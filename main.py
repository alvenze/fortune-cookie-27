#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — write one fortune-cookie line.

The program writes a single line of at most 120 characters to
/output/entry.txt, where the make.fun gate and judge read it.
"""

from pathlib import Path

FORTUNE = (
    "You will try, you will catch, and finally you will read "
    "the whole error message."
)

MAX_CHARS = 120


def validate(text: str) -> None:
    """Hold the fortune to the gate: UTF-8 text, 1 to 120 characters,
    a single line, and not only white space."""
    if not text or not text.strip():
        raise ValueError("fortune is empty")
    if "\n" in text or "\r" in text:
        raise ValueError("fortune must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"fortune is {len(text)} characters, over the {MAX_CHARS} cap")
    text.encode("utf-8")


def output_path() -> Path:
    """The grader mounts /output; when it is not there (a local run),
    fall back to ./output so the program still runs anywhere."""
    root = Path("/output")
    try:
        root.mkdir(parents=True, exist_ok=True)
        return root / "entry.txt"
    except OSError:
        local = Path("output")
        local.mkdir(parents=True, exist_ok=True)
        return local / "entry.txt"


def check(path: Path) -> None:
    """Re-read the written file from disk and verify it byte for byte,
    so a truncated or mangled write can never reach the gate quietly."""
    raw = path.read_bytes()
    if raw != FORTUNE.encode("utf-8"):
        raise ValueError(f"{path} does not match the fortune byte for byte")
    validate(raw.decode("utf-8"))
    print(f"check ok: {path} matches, {len(raw)} bytes")


def main(argv: list[str]) -> None:
    validate(FORTUNE)
    path = output_path()
    path.write_text(FORTUNE, encoding="utf-8")
    print(f"wrote {len(FORTUNE)} chars to {path}")
    if "--check" in argv:
        check(path)


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
