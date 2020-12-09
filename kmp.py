def make_next(pattern):
    nxt = [0 for _ in pattern]
    n = len(pattern)
    i, j = 0, -1
    while i < n - 1:
        if j == -1 or pattern[i] == pattern[j]:
            i += 1
            j += 1
            nxt[i] = j
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

    if j == len(p):
        return i - j
    return -1
