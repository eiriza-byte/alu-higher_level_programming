#!/usr/bin/python3
def multiple_returns(sentence):
    """Return a tuple of (length of sentence, first character)."""
    first_char = sentence[0] if len(sentence) > 0 else None
    return (len(sentence), first_char)
