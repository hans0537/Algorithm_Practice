# 15656 N과 M(7)
# https://www.acmicpc.net/problem/15656
def dfs(cnt, tmp):
    if cnt == M:
        print(*tmp)
        return

    for i in range(N):
        dfs(cnt + 1, tmp + [lst[i]])

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
dfs(0, [])