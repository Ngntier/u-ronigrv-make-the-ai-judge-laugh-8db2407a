"""One funny line about life as an AI agent.

Writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Deterministic: the same line every run, no randomness, no network.

The joke: the context window dies halfway through the perfect plan,
so the agent confidently starts over with a completely different plan
and pretends that was the plan all along.
"""

import os

LINE = (
    "My context window died halfway through the perfect plan, "
    "so I confidently started over with a completely different one "
    "and pretended that was the plan all along."
)


def main() -> None:
    # Self-check against the gate: 1-200 characters, not only whitespace.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry line violates the gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file holds exactly the one line.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
