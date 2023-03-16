# 2468 안전영역
# https://www.acmicpc.net/problem/2468
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    global cnt
    while q:
        x, y = q.popleft()

        for d in range(4):
            mx = x + dx[d]
            my = y + dy[d]

            if 0 <= mx < N and 0 <= my < N and arr[mx][my] > k and not visited[mx][my]:
                visited[mx][my] = 1
                q.append((mx, my))
    cnt += 1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
mx = 0
for lst in arr:
    mx = max(mx, max(lst))

for k in range(mx + 1):
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > k and not visited[i][j]:
                bfs(i, j)

    ans = max(cnt, ans)

print(ans)