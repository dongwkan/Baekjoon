def idx(o):
    return ord(o) - ord("a")

S = input()
n = idx("z") + 1
rst = [-1] * n
i = 0

for c in S:
    if rst[idx(c)] == -1:
        rst[idx(c)] = i
    i += 1

for item in rst:
    print(item, end=" ")
