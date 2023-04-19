# 2589 보물섬
# https://www.acmicpc.net/problem/2589
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(i, j):
    global ans
    v = [[0] * M for _ in range(N)]
    q = deque()
    q.append((i, j))
    v[i][j] = 1

    while q:
        x, y = q.popleft()

        for d in range(4):
            mx = x + dx[d]
            my = y + dy[d]

            if 0 <= mx < N and 0 <= my < M and arr[mx][my] == 'L' and not v[mx][my]:
                q.append((mx, my))
                v[mx][my] = v[x][y] + 1
                ans = max(ans, v[mx][my])

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            bfs(i, j)

print(ans - 1)
