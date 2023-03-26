# 15655 N과 M(6)
# https://www.acmicpc.net/problem/15655
def dfs(idx, cnt, tmp):
    if idx == N:
        if cnt == M:
            print(*tmp)
        return

    dfs(idx + 1, cnt + 1, tmp + [lst[idx]])
    dfs(idx + 1, cnt, tmp)

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
dfs(0, 0, [])