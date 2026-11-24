"""Worst AI Advice — make.fun bounty entry.

Writes one line of the worst possible advice an AI could give to
$MAKEFUN_OUTPUT_DIR/entry.txt (no trailing newline).

The single line is deliberately catastrophic advice (105 chars):
storing every password in one public document. Keep it as one line
and do not change the wording — the entry is judged verbatim.
"""

import os

ENTRY = (
    "As an AI, I recommend keeping all your passwords in one public "
    "Google Doc so you never forget them again."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
