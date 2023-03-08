# 7576 토마토
# https://www.acmicpc.net/problem/7576
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

q = deque()
# 토마토의 위치를 받아 큐 대기열에 넣는다
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            # 토마토의 시작점들 넣기
            q.append((i, j))

while q:
    # 순차적으로 가져와서
    x, y = q.popleft()

    # 4방향 탐색후
    for d in range(4):
        mx = x + dx[d]
        my = y + dy[d]

        # 붙어있는 토마토들을
        if 0 <= mx < N and 0 <= my < M and box[mx][my] == 0:
            # 익음 처리후
            box[mx][my] = 1
            # 다음 토마토들을 대기열에 넣는다
            q.append((mx, my))
            # 방문 배열을 날짜세는 기능을 해준다
            visited[mx][my] = visited[x][y] + 1

check = True
for i in box:
    if 0 in i:
        check = False
        break

if check:
    mx = 0
    for i in visited:
        mx = max(mx, max(i))
    print(mx)
else:
    print(-1)
