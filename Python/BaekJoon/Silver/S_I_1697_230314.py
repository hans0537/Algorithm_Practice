# 1697 숨바꼭질
# https://www.acmicpc.net/problem/1697

def dfs(n, k):
    global ans

    if n == K:
        ans = min(ans, k)
        return

    if ans <= k:
        return

    dfs(n + 1, k + 1)
    dfs(2*n, k + 1)
    if K < n:
        dfs(n - 1, k + 1)

N, K = map(int, input().split())
ans = 1e9
dfs(N, 0)
print(ans)

