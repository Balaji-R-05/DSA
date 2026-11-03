"""
Regenerate LeetCode/README.md, AtCoder/README.md and Codeforces/README.md
from the files actually on disk, so these lists never drift out of sync
with the solutions folders again.

Run manually after adding new solutions:
    python tooling/scripts/generate_readmes.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent

# Titles aren't recoverable from a bare filename, so keep a small local
# lookup seeded from the current README plus any titles found in a
# solution file's first-line comment. Extend this dict when adding a
# problem whose title isn't already discoverable either way.
EXTRA_LEETCODE_TITLES = {
    2144: "Minimum Cost of Buying Candies With Discount",
}


def leetcode_titles_from_readme():
    titles = {}
    readme = ROOT / "LeetCode" / "README.md"
    if readme.exists():
        for line in readme.read_text(encoding="utf-8").splitlines():
            m = re.match(r"-\s+(\d+)\.\s+(.+)", line.strip())
            if m:
                titles[int(m.group(1))] = m.group(2).strip()
    return titles


def leetcode_titles_from_sources():
    titles = {}
    for path in (ROOT / "LeetCode").glob("*/Solution_*.*"):
        first_line = path.read_text(encoding="utf-8", errors="ignore").splitlines()[:1]
        if not first_line:
            continue
        m = re.match(r"[#/\s]+(\d+)\.\s+(.+)", first_line[0])
        if m:
            titles[int(m.group(1))] = m.group(2).strip()
    return titles


def generate_leetcode_readme():
    titles = {}
    titles.update(leetcode_titles_from_sources())
    titles.update(leetcode_titles_from_readme())
    titles.update(EXTRA_LEETCODE_TITLES)

    numbers = set()
    for path in (ROOT / "LeetCode").glob("*/Solution_*.*"):
        m = re.match(r"Solution_(\d+)\.\w+$", path.name)
        if m:
            numbers.add(int(m.group(1)))

    lines = ["# LEETCODE", ""]
    for num in sorted(numbers):
        title = titles.get(num, "TODO: title")
        lines.append(f"- {num}. {title}")

    (ROOT / "LeetCode" / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"LeetCode/README.md: {len(numbers)} problems")


def generate_atcoder_readme():
    contests = {}  # (type_label, number) -> set of letters
    ac = ROOT / "AtCoder"

    for path in ac.glob("ABC/*/ABC_*.*"):
        m = re.match(r"ABC_(\d+)_([A-Z])\.\w+$", path.name)
        if m:
            contests.setdefault(("ABC", int(m.group(1))), set()).add(m.group(2))

    for path in ac.glob("AWC/*/AWC_*.*"):
        m = re.match(r"AWC_(\d+)_([A-Z])\.\w+$", path.name)
        if m:
            contests.setdefault(("AWC", int(m.group(1))), set()).add(m.group(2))

    lines = ["# AtCoder", "", "This folder contains the solutions to the problems on AtCoder.", "",
              "## Solved Problems", ""]
    for (label, num), letters in sorted(contests.items()):
        letters_str = ", ".join(sorted(letters))
        width = 4 if label == "AWC" else 3
        lines.append(f"- **{label} {num:0{width}d}:** {letters_str}")

    (ROOT / "AtCoder" / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"AtCoder/README.md: {len(contests)} contests")


def normalize_cf_id(contest: str, letter: str) -> str:
    return f"{int(contest)}{letter}"


def codeforces_titles_from_readme():
    titles = {}
    readme = ROOT / "Codeforces" / "README.md"
    if readme.exists():
        for line in readme.read_text(encoding="utf-8").splitlines():
            m = re.match(r"-\s+\*\*(\d+)([A-Z]\d?)\*\*\s*-\s*(.+)", line.strip())
            if m:
                titles[normalize_cf_id(m.group(1), m.group(2))] = m.group(3).strip()
    return titles


def codeforces_titles_from_sources():
    titles = {}
    cf = ROOT / "Codeforces"
    for path in cf.glob("Solution_*.*"):
        first_line = path.read_text(encoding="utf-8", errors="ignore").splitlines()[:1]
        if not first_line:
            continue
        m = re.match(r"[#/\s]+(\d+)([A-Z]\d?)\s*[-:]\s*(.+)", first_line[0])
        if m:
            titles[normalize_cf_id(m.group(1), m.group(2))] = m.group(3).strip()
    return titles


def generate_codeforces_readme():
    cf = ROOT / "Codeforces"
    titles = {}
    titles.update(codeforces_titles_from_sources())
    titles.update(codeforces_titles_from_readme())

    ids = set()
    skipped = []
    for path in cf.glob("Solution_*.*"):
        m = re.match(r"Solution_(\d+)([A-Z]\d?)\.\w+$", path.name)
        if m:
            ids.add(normalize_cf_id(m.group(1), m.group(2)))
        else:
            skipped.append(path.name)

    def sort_key(pid):
        m = re.match(r"(\d+)([A-Z]\d?)", pid)
        return (int(m.group(1)), m.group(2))

    lines = ["# Codeforces", "",
              "This repository contains my solutions to various problems from "
              "[Codeforces](https://codeforces.com/).", ""]
    for pid in sorted(ids, key=sort_key):
        title = titles.get(pid)
        lines.append(f"- **{pid}** - {title}" if title else f"- **{pid}**")

    (cf / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Codeforces/README.md: {len(ids)} problems")
    if skipped:
        print(f"  (skipped, doesn't match naming convention: {', '.join(skipped)})")


def main():
    generate_leetcode_readme()
    generate_atcoder_readme()
    generate_codeforces_readme()


if __name__ == "__main__":
    main()
