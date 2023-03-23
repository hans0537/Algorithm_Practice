# 15651 N과 M(3)
# https://www.acmicpc.net/problem/15651
def dfs(cnt, lst):
    if cnt == M:
        print(*lst)
        return

    for i in range(1, N + 1):
        dfs(cnt + 1, lst + [i])

N, M = map(int, input().split())
dfs(0, [])
