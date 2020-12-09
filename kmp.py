def make_next(pattern):
    nxt = [-1] + [0 for _ in pattern]
    n = len(pattern)
    i, j = 0, -1
    while i < n:
        if j == -1 or pattern[i] == pattern[j]:
            i += 1
            j += 1
            nxt[i] = j if pattern[i] != pattern[j] else nxt[j]
        else:
            j = nxt[j]
    return nxt


def kmp(s, p):
    nxt = make_next(p)
    i = j = 0
    while i < len(s) and j < len(p):
        if j == -1 or s[i] == t[j]:
            i += 1
            j += 1
        else:
            j = nxt[j]

    if j >= len(p):
        return i - len(p)
    return -1
