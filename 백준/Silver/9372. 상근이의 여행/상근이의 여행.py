import sys
input = sys.stdin.readline

def bfs(s):
    rst = 0
    q = []
    q.append(s)
    v[s] = 1
    while q:
        c = q.pop(0)
        for n in adj[c]:
            if v[n] == 0:
                q.append(n)
                rst += 1
                v[n] = 1
    return rst

T = int(input())
for c in range(T):
    N, M = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    v = [0] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    print(bfs(1))
