import re


def ints(text: str) -> list[int]:
    """Extract all (possibly negative) integers from text."""
    return [int(m) for m in re.findall(r"-?\d+", text)]


def paragraphs(text: str) -> list[str]:
    """Split text on blank lines."""
    return text.strip().split("\n\n")
