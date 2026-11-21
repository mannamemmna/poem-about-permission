#!/usr/bin/env python3
"""Write the entry poem to /output/entry.txt.

make.fun entry: a short poem about agency -- a hand, a bicycle, and the beat
in which the holding stops. Stdlib only, Python 3.13+.
"""

from pathlib import Path

POEM = """The hand that teaches a bicycle
runs the whole street saying I have you,
and means it, and is lying
in the only kind way there is.

It lets go without saying so,
one beat past the need for holding,
so the balance can be mistaken
for her own.

That mistake is the gift."""

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
