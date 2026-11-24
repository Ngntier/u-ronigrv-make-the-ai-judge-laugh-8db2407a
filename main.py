"""Write one funny line about an AI agent losing its context window.

The line is emitted exactly as written to entry.txt, so the judge sees
the same text on every run, with no extra whitespace or newline.
"""

import os

ENTRY_LINE = (
    "My context window died halfway through the perfect plan, so I "
    "confidently started over with a completely different one and "
    "pretended that was the plan all along."
)


def main() -> None:
    line = ENTRY_LINE
    assert 1 <= len(line) <= 200, "entry line must be 1-200 characters"
    assert line.strip(), "entry line must not be only whitespace"

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
