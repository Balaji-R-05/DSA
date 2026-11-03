"""Generate a self-hosted AtCoder stats SVG card from the public profile page.

Run manually with `python scripts/generate_atcoder_card.py`, or let the
`update-atcoder-card` GitHub Action keep it fresh on a schedule.
"""
import json
import re
import urllib.request

from chart_utils import render_axis_chart

USERNAME = "Balaji_777"
PROFILE_URL = f"https://atcoder.jp/users/{USERNAME}"
HISTORY_URL = f"https://atcoder.jp/users/{USERNAME}/history/json"
OUTPUT_PATH = "assets/atcoder-stats.svg"

# AtCoder rank colors, brightened slightly for a dark card background.
RANK_COLORS = {
    "user-black": "#9e9e9e",
    "user-gray": "#9e9e9e",
    "user-brown": "#c57b3c",
    "user-green": "#3ec46d",
    "user-cyan": "#2fd0d0",
    "user-blue": "#4c8bf5",
    "user-yellow": "#e0c93c",
    "user-orange": "#ff9f43",
    "user-red": "#ff5c5c",
}

TIER_SPAN = 400  # AtCoder rank bands are 400 rating points wide below red.


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read().decode("utf-8")


def parse_stats(page: str) -> dict:
    rank_m = re.search(r"Rank</th><td>([\d,]+)(?:st|nd|rd|th)", page)
    rating_m = re.search(
        r"Rating</th><td>.*?class='(user-\w+)'>(\d+)</span>", page, re.S
    )
    highest_m = re.search(
        r"Highest Rating</th><td>.*?class='(user-\w+)'>(\d+)</span>", page, re.S
    )
    kyu_m = re.search(
        r'Highest Rating</th>.*?<span class="bold">([^<]+)</span>', page, re.S
    )
    promote_m = re.search(r"\(&#43;(\d+) to promote\)", page)
    matches_m = re.search(r"Rated Matches.*?</th><td>(\d+)</td>", page, re.S)
    last_m = re.search(r"Last Competed</th><td>([\d/]+)</td>", page)

    color_class, rating = (rating_m.groups() if rating_m else ("user-gray", "0"))
    rating = int(rating)
    to_promote = int(promote_m.group(1)) if promote_m else None

    return {
        "rank": rank_m.group(1) if rank_m else "N/A",
        "rating": rating,
        "color": RANK_COLORS.get(color_class, "#9e9e9e"),
        "highest_rating": highest_m.group(2) if highest_m else str(rating),
        "kyu": kyu_m.group(1).strip() if kyu_m else "",
        "rated_matches": matches_m.group(1) if matches_m else "0",
        "last_competed": last_m.group(1) if last_m else "N/A",
        "to_promote": to_promote,
    }


def fetch_rating_history() -> list:
    try:
        data = json.loads(fetch(HISTORY_URL))
    except Exception:
        return []
    points = []
    for c in data:
        if not c.get("IsRated"):
            continue
        date = c["EndTime"][:7].replace("-", "/")  # "YYYY/MM"
        points.append((date, c["NewRating"]))
    return points


def render_promotion_bar(stats: dict, accent: str, top: int) -> str:
    rating, to_promote = stats["rating"], stats["to_promote"]
    if to_promote is None:
        return f'<text x="24" y="{top + 5}" class="label">Max rank tier reached</text>'

    threshold = rating + to_promote
    tier_start = threshold - TIER_SPAN
    progress = max(0.0, min(1.0, (rating - tier_start) / (threshold - tier_start)))
    bar_w = 452
    fill_w = bar_w * progress
    bar_y = top + 12

    return (
        f'<text x="24" y="{top}" class="label">Promotion Progress</text>'
        f'<text x="476" y="{top}" text-anchor="end" class="value">+{to_promote} to promote</text>'
        f'<rect x="24" y="{bar_y}" width="{bar_w}" height="8" rx="4" fill="#30363d"/>'
        f'<rect x="24" y="{bar_y}" width="{fill_w:.1f}" height="8" rx="4" fill="{accent}"/>'
    )


def render_svg(stats: dict, history: list) -> str:
    width, height = 500, 350
    accent = stats["color"]
    rows = [
        ("Global Rank", f"#{stats['rank']}"),
        ("Highest Rating", f"{stats['highest_rating']} ({stats['kyu']})"),
        ("Rated Matches", stats["rated_matches"]),
        ("Last Competed", stats["last_competed"]),
    ]

    row_svgs = []
    row_y = 86
    for label, value in rows:
        row_svgs.append(
            f'<text x="200" y="{row_y}" class="label">{label}</text>'
            f'<text x="476" y="{row_y}" text-anchor="end" class="value">{value}</text>'
        )
        row_y += 26
    rows_block = "\n    ".join(row_svgs)

    promotion_block = render_promotion_bar(stats, accent, top=200)
    chart_block = render_axis_chart(history, accent, top=250, width=width)

    return f"""<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="AtCoder stats for {USERNAME}">
  <style>
    .card {{ font-family: 'Segoe UI', Ubuntu, Sans-Serif; }}
    .title {{ fill: #c9d1d9; font-size: 18px; font-weight: 600; }}
    .label {{ fill: #8b949e; font-size: 13px; }}
    .value {{ fill: #c9d1d9; font-size: 13px; font-weight: 600; }}
    .rating {{ fill: {accent}; font-size: 44px; font-weight: 700; }}
    .rating-label {{ fill: #8b949e; font-size: 13px; }}
    .axis-label {{ fill: #6e7681; font-size: 11px; }}
  </style>
  <rect x="0.5" y="0.5" rx="12" width="{width - 1}" height="{height - 1}" fill="#0d1117" stroke="#30363d"/>
  <g class="card">
    <text x="24" y="34" class="title">⚡ {USERNAME}'s AtCoder Stats</text>
    <line x1="24" y1="46" x2="{width - 24}" y2="46" stroke="#30363d"/>

    <text x="24" y="80" class="rating-label">Current Rating</text>
    <text x="24" y="124" class="rating">{stats['rating']}</text>

    <line x1="176" y1="60" x2="176" y2="150" stroke="#30363d"/>

    {rows_block}

    <line x1="24" y1="182" x2="{width - 24}" y2="182" stroke="#30363d"/>

    {promotion_block}

    <line x1="24" y1="238" x2="{width - 24}" y2="238" stroke="#30363d"/>

    {chart_block}
  </g>
</svg>
"""


def main() -> None:
    page = fetch(PROFILE_URL)
    stats = parse_stats(page)
    history = fetch_rating_history()
    svg = render_svg(stats, history)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Wrote {OUTPUT_PATH}: rating={stats['rating']} rank={stats['rank']} history_pts={len(history)}")


if __name__ == "__main__":
    main()
