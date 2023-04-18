# 16918 봄버맨
# https://www.acmicpc.net/problem/16918
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(lst):
    q = deque(lst)
    v = [[0] * C for _ in range(R)]

    while q:
        x, y = q.popleft()
        v[x][y] = 1
        arr[x][y] = '.'

        for d in range(4):
            mx = x + dx[d]
            my = y + dy[d]

            if 0 <= mx < R and 0 <= my < C and not v[mx][my]:
                arr[mx][my] = '.'


R, C, N = map(int, input().split())
arr = [list(input()) for _ in range(R)]

# 2번 부터 시작
time = 1
while time < N:
    # 폭탄이 설치 되어있지 않은 모든칸에 폭탄을 설치 하면서
    # 직전의 폭탄의 위치를 저장
    lst = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] == '.':
                arr[i][j] = 'O'
            else:
                lst.append((i, j))

    time += 1

    if time == N:
        break
    # 폭탄 터트리기
    bfs(lst)

    time += 1


for lst in arr:
    print(''.join(lst))

