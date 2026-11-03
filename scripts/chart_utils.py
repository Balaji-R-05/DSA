"""Shared axis-chart renderer for the stats cards (gridlines, tick labels, date labels)."""
import math


def _nice_ticks(lo: float, hi: float, n: int = 4) -> list:
    if hi <= lo:
        hi = lo + 1
    raw_step = (hi - lo) / n
    magnitude = 10 ** math.floor(math.log10(raw_step))
    residual = raw_step / magnitude
    nice = 10 if residual > 5 else 5 if residual > 2 else 2 if residual > 1 else 1
    step = nice * magnitude

    nice_lo = math.floor(lo / step) * step
    nice_hi = math.ceil(hi / step) * step

    ticks = []
    v = nice_lo
    while v <= nice_hi + step * 1e-6:
        ticks.append(v)
        v += step
    return ticks


def render_axis_chart(points: list, accent: str, top: int, width: int = 500, grid_color: str = "#30363d") -> str:
    """points: list of (date_label, value) tuples, oldest first."""
    if len(points) < 2:
        return f'<text x="24" y="{top + 20}" class="label">Not enough contest history yet</text>'

    values = [v for _, v in points]
    x0, chart_w, chart_h = 50, width - 50 - 24, 70
    ticks = _nice_ticks(min(values), max(values))
    nice_lo, nice_hi = ticks[0], ticks[-1]

    def y_of(v):
        return top + chart_h - ((v - nice_lo) / (nice_hi - nice_lo)) * chart_h

    grid = []
    for t in ticks:
        y = y_of(t)
        label = f"{t:.0f}"
        grid.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x0 + chart_w}" y2="{y:.1f}" stroke="{grid_color}" stroke-width="1"/>')
        grid.append(f'<text x="{x0 - 8}" y="{y + 4:.1f}" text-anchor="end" class="axis-label">{label}</text>')

    pts = []
    for i, (_, v) in enumerate(points):
        x = x0 + (i / (len(points) - 1)) * chart_w
        y = y_of(v)
        pts.append((x, y))
    polyline = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)

    first_date, last_date = points[0][0], points[-1][0]
    date_y = top + chart_h + 16

    return "".join(grid) + (
        f'<polyline points="{polyline}" fill="none" stroke="{accent}" stroke-width="2.5" '
        f'stroke-linejoin="round" stroke-linecap="round"/>'
        f'<text x="{x0}" y="{date_y}" class="axis-label">{first_date}</text>'
        f'<text x="{x0 + chart_w}" y="{date_y}" text-anchor="end" class="axis-label">{last_date}</text>'
    )
