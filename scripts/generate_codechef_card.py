"""Generate a self-hosted CodeChef stats SVG card from the public profile page.

Run manually with `python scripts/generate_codechef_card.py`, or let the
`update-codechef-card` GitHub Action keep it fresh on a schedule.
"""
import json
import re
import urllib.request

from chart_utils import render_axis_chart

USERNAME = "lord_grim_777"
PROFILE_URL = f"https://www.codechef.com/users/{USERNAME}"
OUTPUT_PATH = "assets/codechef-stats.svg"

STAR_COLORS = {
    1: "#9e9e9e",
    2: "#3ec46d",
    3: "#2fd0d0",
    4: "#4c8bf5",
    5: "#e0c93c",
    6: "#ff9f43",
    7: "#ff5c5c",
}

# Public CodeChef star rating bands.
STAR_BANDS = [
    (1, 0, 1400),
    (2, 1400, 1600),
    (3, 1600, 1800),
    (4, 1800, 2000),
    (5, 2000, 2200),
    (6, 2200, 2500),
    (7, 2500, None),
]


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read().decode("utf-8")


def parse_stats(page: str) -> dict:
    rating_m = re.search(r"<div class=\"rating-number\">\s*(\d+)", page)
    stars_m = re.search(r"(\d+)&#9733;", page)
    highest_m = re.search(r"\(Highest Rating (\d+)\)", page)
    ranks_m = re.search(
        r'<strong>\s*(\d+)\s*</strong>\s*</a>\s*Global Rank.*?'
        r'<strong>\s*(\d+)\s*</strong>\s*</a>\s*Country Rank',
        page,
        re.S,
    )
    solved_m = re.search(r"Total Problems Solved:\s*(\d+)", page)
    history_m = re.search(r'"date_versus_rating":\{"all":(\[.*?\])', page, re.S)

    rating = int(rating_m.group(1)) if rating_m else 0
    stars = int(stars_m.group(1)) if stars_m else 1
    history = []
    if history_m:
        try:
            history = [
                (c["end_date"][:7].replace("-", "/"), int(c["rating"]))
                for c in json.loads(history_m.group(1))
            ]
        except Exception:
            history = []

    return {
        "rating": rating,
        "stars": stars,
        "highest_rating": int(highest_m.group(1)) if highest_m else rating,
        "global_rank": ranks_m.group(1) if ranks_m else "N/A",
        "country_rank": ranks_m.group(2) if ranks_m else "N/A",
        "solved": solved_m.group(1) if solved_m else "N/A",
        "history": history,
    }


def promotion_info(rating: int, stars: int):
    for tier, lo, hi in STAR_BANDS:
        if tier == stars and hi is not None:
            return hi - rating, lo, hi
    return None, None, None


def render_star_row(stars: int, accent: str, top: int, width: int) -> str:
    n = 7
    gap = 20
    start_x = (width - (n - 1) * gap) / 2
    glyphs = []
    for i in range(1, n + 1):
        fill = accent if i <= stars else "#4a3a30"
        x = start_x + (i - 1) * gap
        glyphs.append(f'<text x="{x:.1f}" y="{top}" text-anchor="middle" class="star" fill="{fill}">★</text>')
    return "".join(glyphs)


def render_rating_banner(stats: dict, accent: str, top: int, width: int) -> str:
    x, w, h = 24, width - 48, 64
    return (
        f'<rect x="{x}" y="{top}" width="{w}" height="{h}" rx="12" fill="{accent}" fill-opacity="0.12" '
        f'stroke="{accent}" stroke-opacity="0.4"/>'
        f'<text x="{x + 20}" y="{top + 22}" class="label">Current Rating</text>'
        f'<text x="{x + 20}" y="{top + 54}" class="rating">{stats["rating"]}</text>'
        f'<text x="{x + w - 20}" y="{top + 22}" text-anchor="end" class="value">{stats["stars"]}★ Coder</text>'
        f'<text x="{x + w - 20}" y="{top + 54}" text-anchor="end" class="label">Highest {stats["highest_rating"]}</text>'
    )


def render_tiles(tiles: list, accent: str, top: int, width: int) -> str:
    n = len(tiles)
    gap = 8
    x0, full_w = 24, width - 48
    tile_w = (full_w - gap * (n - 1)) / n
    blocks = []
    for i, (label, value) in enumerate(tiles):
        tx = x0 + i * (tile_w + gap)
        cx = tx + tile_w / 2
        blocks.append(
            f'<rect x="{tx:.1f}" y="{top}" width="{tile_w:.1f}" height="56" rx="8" '
            f'fill="{accent}" fill-opacity="0.06" stroke="{accent}" stroke-opacity="0.25"/>'
            f'<text x="{cx:.1f}" y="{top + 22}" text-anchor="middle" class="label">{label}</text>'
            f'<text x="{cx:.1f}" y="{top + 44}" text-anchor="middle" class="tile-value">{value}</text>'
        )
    return "".join(blocks)


def render_promotion_bar(stats: dict, accent: str, top: int) -> str:
    to_promote, lo, hi = promotion_info(stats["rating"], stats["stars"])
    if to_promote is None:
        return f'<text x="24" y="{top + 5}" class="label">Max star tier reached</text>'

    progress = max(0.0, min(1.0, (stats["rating"] - lo) / (hi - lo)))
    bar_w = 452
    fill_w = bar_w * progress
    bar_y = top + 12

    return (
        f'<text x="24" y="{top}" class="label">Promotion Progress</text>'
        f'<text x="476" y="{top}" text-anchor="end" class="value">+{to_promote} to {stats["stars"] + 1}★</text>'
        f'<rect x="24" y="{bar_y}" width="{bar_w}" height="8" rx="4" fill="#3a2a20"/>'
        f'<rect x="24" y="{bar_y}" width="{fill_w:.1f}" height="8" rx="4" fill="{accent}"/>'
    )


def render_svg(stats: dict) -> str:
    width, height = 500, 400
    accent = STAR_COLORS.get(stats["stars"], "#9e9e9e")
    tiles = [
        ("Global Rank", f"#{stats['global_rank']}"),
        ("Country Rank", f"#{stats['country_rank']}"),
        ("Rated Contests", str(len(stats["history"]))),
        ("Solved", stats["solved"]),
    ]

    star_row = render_star_row(stats["stars"], accent, top=66, width=width)
    banner_block = render_rating_banner(stats, accent, top=84, width=width)
    tiles_block = render_tiles(tiles, accent, top=166, width=width)
    promotion_block = render_promotion_bar(stats, accent, top=246)
    chart_block = render_axis_chart(stats["history"], accent, top=296, width=width, grid_color="#3a2a20")

    return f"""<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="CodeChef stats for {USERNAME}">
  <defs>
    <linearGradient id="topbar" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{accent}" stop-opacity="0.9"/>
      <stop offset="1" stop-color="{accent}" stop-opacity="0.25"/>
    </linearGradient>
    <clipPath id="round"><rect x="0" y="0" width="{width}" height="{height}" rx="18"/></clipPath>
  </defs>
  <style>
    .card {{ font-family: 'Segoe UI', Ubuntu, Sans-Serif; }}
    .title {{ fill: #f0e6dd; font-size: 18px; font-weight: 600; }}
    .label {{ fill: #b8a999; font-size: 12px; }}
    .value {{ fill: #f0e6dd; font-size: 13px; font-weight: 600; }}
    .tile-value {{ fill: #f0e6dd; font-size: 15px; font-weight: 700; }}
    .rating {{ fill: {accent}; font-size: 32px; font-weight: 700; }}
    .star {{ font-size: 18px; }}
    .axis-label {{ fill: #8c7a6a; font-size: 11px; }}
  </style>
  <g clip-path="url(#round)">
    <rect x="0" y="0" width="{width}" height="{height}" fill="#1a110c"/>
    <rect x="0" y="0" width="{width}" height="4" fill="url(#topbar)"/>
  </g>
  <rect x="0.5" y="0.5" rx="18" width="{width - 1}" height="{height - 1}" fill="none" stroke="{accent}" stroke-opacity="0.35"/>
  <g class="card">
    <text x="24" y="34" class="title">♟ {USERNAME}</text>
    <text x="476" y="34" text-anchor="end" class="label">CodeChef</text>
    <line x1="24" y1="46" x2="{width - 24}" y2="46" stroke="#3a2a20" stroke-dasharray="3,3"/>

    {star_row}

    {banner_block}

    {tiles_block}

    {promotion_block}

    <line x1="24" y1="282" x2="{width - 24}" y2="282" stroke="#3a2a20" stroke-dasharray="3,3"/>

    {chart_block}
  </g>
</svg>
"""


def main() -> None:
    page = fetch(PROFILE_URL)
    stats = parse_stats(page)
    svg = render_svg(stats)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(svg)
    print(
        f"Wrote {OUTPUT_PATH}: rating={stats['rating']} stars={stats['stars']} "
        f"history_pts={len(stats['history'])}"
    )


if __name__ == "__main__":
    main()
