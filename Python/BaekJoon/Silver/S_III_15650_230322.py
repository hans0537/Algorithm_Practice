# 15650 N과 M(2)
# https://www.acmicpc.net/problem/15650
# def check(lst):
#     for i in range(len(lst) - 1):
#         for j in range(i + 1, len(lst)):
#             if lst[i] > lst[j]:
#                 return False
#     return True
#
# def dfs(n, lst):
#     if n == M:
#         if check(lst):
#             print(*lst)
#         return
#
#     for j in range(1, N + 1):
#         if not visited[j]:
#             visited[j] = 1
#             dfs(n + 1, lst + [j])
#             visited[j] = 0

def dfs(n, lst):
    if n > N:
        if len(lst) == M:
            print(*lst)
        return

    dfs(n + 1, lst + [n])
    dfs(n + 1, lst)


N, M = map(int, input().split())
dfs(1, [])
