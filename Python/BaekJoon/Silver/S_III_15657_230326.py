# 15657 N과 M(8)
# https://www.acmicpc.net/problem/15657

def dfs(cnt, cidx, tmp):
    if cnt == M:
        print(*tmp)
        return

    for i in range(cidx, N):
        dfs(cnt + 1, i, tmp + [lst[i]])

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
dfs(0, 0, [])