def clip(n: int, start=0, end=180):
    if n <= start:
        return start
    elif n >= end:
        return end
    return n
