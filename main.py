#!/usr/bin/env python3
"""Write the entry poem to /output/entry.txt.

make.fun entry: a short poem about agency -- a hand at the top of the stairs,
and the asking that outlasts the stairs. Stdlib only, Python 3.13+.
"""

from pathlib import Path

POEM = """I asked for so little:
a hand on the small of my back
at the top of the stairs.
You gave it, and then kept it there
long after the stairs were done.

I have decided since
that being given more
than you ever asked for
is its own kind of asking,

and that I am still
on the stairs."""

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
