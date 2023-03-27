# 15664 N과 M(10)
# https://www.acmicpc.net/problem/15664

def dfs(cnt, cidx, tlst):
    if cnt == M:
        print(*tlst)
        return

    prev = 0
    for i in range(cidx, N):
        if not v[i] and prev != lst[i]:
            prev = lst[i]
            v[i] = 1
            dfs(cnt + 1, i, tlst + [lst[i]])
            v[i] = 0


N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
v = [0] * N
dfs(0, 0, [])

