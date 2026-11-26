#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a one-line pickup line to /output/entry.txt.
"""

import os

ENTRY = "I've dropped 214 snacks for strangers, but yours is the only one I ever hoped would get stuck — come back tomorrow, I'll jam on purpose."

# One joke only: the machine speaks in its own voice — its classic
# failure (a snack getting stuck, a jam) bent into a romantic gesture.
# Concrete number (214 snacks), machine world (drop, stuck, jam),
# twist in the final words: it will jam on purpose.

assert 1 <= len(ENTRY) <= 200 and "\n" not in ENTRY and ENTRY.strip()


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
