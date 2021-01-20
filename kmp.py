def make_next(pattern):
    nxt = [0 for _ in pattern]
    k = 0
    for q in range(1, len(pattern)):
      while k > 0 and pattern[k] != pattern[q]:
        k = nxt[k-1]
      if pattern[k] == pattern[q]:
        k += 1
      nxt[q] = k
    return nxt


def kmp(s, p):
    nxt = make_next(p)
    print(nxt)
    matched = 0
    for idx, each in enumerate(s):
      if matched == len(p):
        return idx - len(p)
      if each == p[matched]:
        matched += 1
      else:
        while matched and each != p[matched]:
          matched = nxt[matched - 1]
        if each == p[matched]:
          matched += 1
    if matched == len(p):
      return len(s) - matched
    return -1
