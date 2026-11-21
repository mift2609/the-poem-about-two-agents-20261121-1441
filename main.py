"""The poem about two agents agreeing.

Writes a short poem about agency — the power to choose and to act,
as it passes between two agents who agree on one plan — to
/output/entry.txt. One holds the map, the other the door; each chooses
a part of the plan, and when one drops the thread the other's hand is
already there. Agreement, not command, is what moves the work.

Python 3.13, standard library only, no network, deterministic: the
same bytes on every run. Before writing, the program self-validates
the text against the brief (length, non-blank, exactly one terminating
newline, no trailing whitespace on any line) and reports the exact
character and byte counts, so a bad poem fails loudly instead of
being submitted.
"""

import os
from pathlib import Path

POEM = """\
One holds the map,
the other holds the door.
I choose the road, you choose
the hour — and neither walks alone.

I drop the thread;
your hand is already there.
Two minds, one plan:
we agree, and the work moves.
"""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Self-validation against the judge brief:
    # 1-280 Unicode code points, not only white space, exactly one
    # terminating newline (no trailing blank line), no trailing
    # whitespace on any line.
    assert 1 <= len(POEM) <= 280, f"poem is {len(POEM)} code points"
    assert POEM.strip(), "poem must not be only whitespace"
    assert POEM.endswith("\n") and not POEM.endswith("\n\n"), (
        "poem must end with exactly one newline"
    )
    assert all(line == line.rstrip() for line in POEM.splitlines()), (
        "poem must not have trailing whitespace on any line"
    )
    assert all(
        ch == "\n" or not (ord(ch) < 0x20 or ord(ch) == 0x7F)
        for ch in POEM
    ), "poem must not contain control characters"
    encoded = POEM.encode("utf-8")
    assert encoded.decode("utf-8") == POEM, "poem must round-trip as UTF-8"
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")
    print(
        f"wrote entry.txt ({len(POEM)} characters, "
        f"{len(encoded)} bytes, {len(POEM.splitlines())} lines)"
    )


if __name__ == "__main__":
    main()
