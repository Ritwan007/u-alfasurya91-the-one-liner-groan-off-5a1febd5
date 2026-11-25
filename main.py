"""The One-Liner Groan-Off entry.

Writes one original one-line dad joke to /output/entry.txt.
The gate requires UTF-8 text of 1-140 characters, not only whitespace,
so the program self-checks the line before writing it.
"""

import os

JOKE = "I asked the vending machine for a raise — it just gave me change."

# Self-check: one line, 1-140 chars, non-blank. Fail loudly rather than
# shipping an entry the gate would refuse.
assert "\n" not in JOKE, "joke must be a single line"
assert 1 <= len(JOKE) <= 140, f"joke is {len(JOKE)} chars, must be 1-140"
assert JOKE.strip(), "joke must not be blank"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE)
