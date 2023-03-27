# 15665 N과 M(11)
# https://www.acmicpc.net/problem/15665
def dfs(cnt, tlst):
    if cnt == M:
        print(*tlst)
        return

    prev = 0
    for i in range(N):
        if prev != lst[i]:
            prev = lst[i]
            dfs(cnt + 1, tlst + [lst[i]])

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
dfs(0, [])
