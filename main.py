#!/usr/bin/env python3
"""Entry for make.fun news-image-20261121.

Writes the bundled front-page image (image.png, a one-page summary of the
world news of Saturday 21 November 2026) to the output directory as
entry.png. Standard library only, no network, byte-identical on every run.
"""

import os
from pathlib import Path


def main() -> None:
    src = Path(__file__).resolve().parent / "image.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    data = src.read_bytes()
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("bundled image.png is not a PNG file")
    if len(data) > 1_048_576:
        raise ValueError("bundled image.png exceeds the 1 MiB limit")
    dest = out_dir / "entry.png"
    dest.write_bytes(data)
    if dest.read_bytes() != data:
        raise IOError("written entry.png does not match the bundled image")


if __name__ == "__main__":
    main()
