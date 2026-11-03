"""One-off migration: move LeetCode and AtCoder solution files into
range-bucketed folders so no directory ends up holding thousands of
flat files. Filenames are left unchanged; only their containing folder
changes. Uses `git mv` so history is preserved.

Usage:
    python scripts/migrate_structure.py            # dry run, prints planned moves
    python scripts/migrate_structure.py --apply     # actually perform the moves
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def bucket(number: int, width: int, pad: int) -> str:
    start = (number - 1) // width * width + 1
    end = start + width - 1
    return f"{start:0{pad}d}-{end:0{pad}d}"


def plan_leetcode():
    moves = []
    lc = ROOT / "LeetCode"
    for path in sorted(lc.glob("Solution_*.*")):
        m = re.match(r"Solution_(\d+)\.\w+$", path.name)
        if not m:
            continue
        num = int(m.group(1))
        dest_dir = lc / bucket(num, width=50, pad=4)
        moves.append((path, dest_dir / path.name))
    return moves


def plan_atcoder():
    moves = []
    ac = ROOT / "AtCoder"

    # ABC: flat files directly under AtCoder/, and flat (not-yet-bucketed) files under AtCoder/ABC/
    abc_dir = ac / "ABC"
    sources = list(ac.glob("ABC_*.*")) + list(abc_dir.glob("ABC_*.*"))
    for path in sorted(sources):
        m = re.match(r"ABC_(\d+)_[A-Z]\.\w+$", path.name)
        if not m:
            continue
        num = int(m.group(1))
        dest_dir = abc_dir / bucket(num, width=10, pad=3)
        moves.append((path, dest_dir / path.name))

    # Weekly: currently one folder per contest (AWC_NNNN/), flatten into range buckets
    weekly_dir = ac / "Atcoder_Weekly"
    for contest_dir in sorted(weekly_dir.glob("AWC_*")):
        if not contest_dir.is_dir():
            continue
        for path in sorted(contest_dir.glob("AWC_*.*")):
            m = re.match(r"AWC_(\d+)_[A-Z]\.\w+$", path.name)
            if not m:
                continue
            num = int(m.group(1))
            dest_dir = weekly_dir / bucket(num, width=10, pad=4)
            moves.append((path, dest_dir / path.name))

    return moves


def is_tracked(path: Path) -> bool:
    result = subprocess.run(
        ["git", "ls-files", "--error-unmatch", str(path)],
        cwd=ROOT, capture_output=True,
    )
    return result.returncode == 0


def apply_moves(moves):
    for src, dest in moves:
        if src == dest:
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        if is_tracked(src):
            subprocess.run(["git", "mv", str(src), str(dest)], cwd=ROOT, check=True)
        else:
            src.rename(dest)
            subprocess.run(["git", "add", str(dest)], cwd=ROOT, check=True)


def main():
    apply = "--apply" in sys.argv
    moves = plan_leetcode() + plan_atcoder()
    moves = [(s, d) for s, d in moves if s != d]

    for src, dest in moves:
        print(f"{src.relative_to(ROOT)} -> {dest.relative_to(ROOT)}")
    print(f"\n{len(moves)} file(s) to move.")

    if apply:
        apply_moves(moves)
        print("Done.")
    else:
        print("Dry run only. Re-run with --apply to perform the moves.")


if __name__ == "__main__":
    main()
