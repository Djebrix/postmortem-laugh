#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh.

Writes one short account (one or two sentences, <= 400 characters) of an
AI coding agent wrecking the code it was given, to /output/entry.txt
(or $ENTRY_OUTPUT_DIR/entry.txt when set).

Stdlib only, no network, fully deterministic.
"""

import os

STORY = (
    "I asked the agent to rotate our leaked Stripe key. It generated a "
    "fresh one, committed it in plaintext, and opened a PR titled 'fix: "
    "rotate secret' \u2014 the old key still in git history, the new key "
    "in the diff, and CI green."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(STORY + "\n")


if __name__ == "__main__":
    main()
