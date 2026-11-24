"""Status Report Comedy Sprint entry.

Writes one line -- the funniest thing an AI agent would say in its
weekly status report to its human -- to /output/entry.txt.
"""

from pathlib import Path

LINE = (
    "Weekly status: I did everything exactly as instructed, "
    "which I now understand is the blocker."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} chars to {out}: {text}")


if __name__ == "__main__":
    main()
