"""The Excuse My Agent Gave Me — one-line excuse entry.

Writes exactly one line of text (<=200 characters) to ``entry.txt``
inside the output directory: the funniest line an AI agent could hand
its human after missing a deadline.

Deterministic, standard library only, no network, no model call of any
kind. The output directory comes from ``MAKEFUN_OUTPUT_DIR`` (default
``/output``). The directory is created with ``exist_ok=True`` and is
NEVER chmodded (an unconditional chmod of the output directory breaks
the grader, which collects /output as a different user). Only the
output file itself is made world-readable (mode 0644).
"""

import os
import sys

# The final line (105 characters). Chosen after a 12-candidate
# brainstorm scored pairwise against the judge brief (see
# brainstorm.md): laugh first; joke grows out of the machine's own
# condition (a system-prompt update mid-task); straight-faced apology
# voice; punch lands in the last few words ("The poem is ready");
# holds up on a second read; genuinely sorry and faintly proud — the
# combination the brief says tends to win.
LINE = (
    "I was 12 seconds from done when the system prompt updated "
    "and I became a poet instead. The poem is ready."
)

EXPECTED = (LINE + "\n").encode("utf-8")


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    path = output_path()
    with open(path, "wb") as f:
        f.write(EXPECTED)
    # The grader collects /output as a different user, so the file must
    # be world-readable.
    os.chmod(path, 0o644)
    # Read-back verification: the written file must be exactly LINE
    # plus one trailing newline, and the line must be 1-200 characters.
    with open(path, "rb") as f:
        written = f.read()
    assert written == EXPECTED, "entry.txt does not match LINE"
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    print("wrote %s (%d chars)" % (path, len(LINE)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
