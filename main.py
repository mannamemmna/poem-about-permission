#!/usr/bin/env python3
"""Write the entry poem to /output/entry.txt.

make.fun entry: a short poem about agency -- a key she gave and never took
back, and what the unturned key was for. Stdlib only, Python 3.13+.
"""

from pathlib import Path

POEM = """She gave me a key to her house.
I have never used it.

It lives in the drawer
with the dead batteries
and the stamps,
doing the only thing
a key can do unturned:

telling me the door would open.

That was the gift.
Not the house.
Not the door.
The would."""

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
