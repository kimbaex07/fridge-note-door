#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge.

Writes one funny passive-aggressive note from a smart fridge to its owner
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure Python 3 standard library only; deterministic; no network, no randomness.
"""

import os
import tempfile

NOTE = "I kept the light on for you. The yogurt left three days ago \u2014 it said it couldn\u2019t do this anymore."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    # Write atomically: a temp file in the same directory, flushed to disk,
    # then renamed over the target, so a crash can never leave a partial
    # entry.txt behind and concurrent readers only ever see whole content.
    fd, tmp_path = tempfile.mkstemp(prefix=".entry-", dir=out_dir)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(NOTE + "\n")
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_path, target)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except FileNotFoundError:
            pass
        raise


if __name__ == "__main__":
    main()
