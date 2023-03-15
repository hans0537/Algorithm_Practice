# 2178 미로탐색
# https://www.acmicpc.net/problem/2178
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1

    while q:
        x, y = q.popleft()

        if x == N - 1 and y == M - 1:
            print(visited[x][y])
            return

        for d in range(4):
            mx = x + dx[d]
            my = y + dy[d]

            if 0 <= mx < N and 0 <= my < M and arr[mx][my] == 1 and not visited[mx][my]:
                visited[mx][my] = visited[x][y] + 1
                q.append((mx, my))


N, M = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
bfs(0,0)
