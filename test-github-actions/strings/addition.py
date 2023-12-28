def add_strings(a: str, b: str) -> str:
    if len(a) == 0 or len(b) == 0:
        raise ValueError('Empty string')
    return a + b
