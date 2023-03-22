# 15649 N과 M(1)
# https://www.acmicpc.net/problem/15649

def dfs(n, lst):
    # 선택된 숫자의 개수가 M개일때 종료
    if n == M:
        print(*lst)
        return

    # 1 부터 N 까지 선택해나간다
    for j in range(1, N + 1):
        if not visited[j]:
            visited[j] = 1
            dfs(n + 1, lst + [j])
            visited[j] = 0

N, M = map(int, input().split())
visited = [0] * (N + 1)
dfs(0, [])
