# 15666 N과 M(12)
# https://www.acmicpc.net/problem/15666
def dfs(cnt, cidx, tlst):
    if cnt == M:
        print(*tlst)
        return

    prev = 0
    for i in range(cidx, N):
        if prev != lst[i]:
            prev = lst[i]
            dfs(cnt + 1, i, tlst + [lst[i]])

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
dfs(0, 0, [])
