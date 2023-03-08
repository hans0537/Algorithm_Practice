# 7576 토마토
# https://www.acmicpc.net/problem/7576
from collections import deque

M, N, H = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N * H)]
visited = [[0] * M for _ in range(N * H)]

# 상 하 좌 우 위층 아래층
dx = [-1, 1, 0, 0, -N, N]
dy = [0, 0, -1, 1, 0, 0]

q = deque()
# 토마토의 위치를 받아 큐 대기열에 넣는다
for i in range(N * H):
    for j in range(M):
        if box[i][j] == 1:
            # 토마토의 시작점들 넣기
            q.append((i, j))

while q:
    # 순차적으로 가져와서
    x, y = q.popleft()

    # 6방향 탐색후
    for d in range(6):

        # 배열 속에서 층 분리로 인해 만약 현재 위치가 N을 벗어나면
        # 위로 올라가는것을 방지하기 위함
        if x % N == 0 and d == 0:
            continue

        # 배열 속에서 층 분리로 인해 만약 현재 위치가 N을 벗어나면
        # 내려가는것을 방지하기 위함
        if (x + 1) % N == 0 and d == 1:
            continue

        mx = x + dx[d]
        my = y + dy[d]

        # 붙어있는 토마토들을
        if 0 <= mx < N*H and 0 <= my < M and box[mx][my] == 0:
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
