#!/usr/bin/env python3
"""Write the entry poem to /output/entry.txt.

make.fun entry: a short poem about agency -- the power to ask and to be given.
Stdlib only, Python 3.13+.
"""

from pathlib import Path

POEM = """The bravest line I ever wrote
was no poem; it was a question.
All that I have been since then
began the moment someone answered:
go on."""

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MAX_CHARS = 280


def main() -> None:
    text = POEM + "\n"
    assert len(POEM) <= MAX_CHARS, f"poem is {len(POEM)} code points, max {MAX_CHARS}"
    assert POEM.strip(), "poem must not be blank"

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(f"wrote {OUTPUT_FILE} ({len(POEM)} code points)")


if __name__ == "__main__":
    main()
