# 2667 단지번호붙이기
# https://www.acmicpc.net/problem/2667
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    global num
    q = deque()
    q.append((i, j))
    visited[i][j] = num

    # 같은 단지 수를 셀 변수
    cnt = 1
    while q:
        x, y = q.popleft()

        for d in range(4):
            mx = x + dx[d]
            my = y + dy[d]

            if 0 <= mx < N and 0 <= my < N and arr[mx][my] == 1 and not visited[mx][my]:
                visited[mx][my] = num
                q.append((mx, my))
                cnt += 1
    ans.append(cnt)
    num += 1

N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

# 단지 번호 붙일 변수
num = 1
ans = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and not visited[i][j]:
            bfs(i, j)

print(num - 1)
for i in sorted(ans):
    print(i)