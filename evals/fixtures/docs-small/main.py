"""Tiny, non-networked fixture for documentation audits."""

def summarize(items: list[str]) -> int:
    """Return the number of items supplied."""
    return len(items)


if __name__ == "__main__":
    print("Star Notes fixture: ready for manual inspection")
