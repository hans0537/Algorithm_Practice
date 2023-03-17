# 2573 빙산
# https://www.acmicpc.net/problem/2573
from collections import deque
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    cnt = 0
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and not visited[i][j]:
                q = deque()
                q.append((i, j))
                visited[i][j] = 1

                while q:
                    x, y = q.popleft()

                    for d in range(4):
                        mx = x + dx[d]
                        my = y + dy[d]

                        if 0 <= mx < N and 0 <= my < M and arr[mx][my] != 0 and not visited[mx][my]:
                            visited[mx][my] = 1
                            q.append((mx, my))

                cnt += 1

    return cnt

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
while True:
    # 빙산 덩어리 방문 작업 체크
    blocks = bfs()
    
    # 두덩어리로 나뉘기 전에 다 녹아버림
    if blocks == 0:
        ans = 0
        break
    # 덩어리가 두개 이상이 됨
    elif blocks >= 2:
        break
    else:
        # 아직 덩어리가 1개 이면
        # 임시 배열에 복사한 후 녹이기 시전
        temp = copy.deepcopy(arr)
        for i in range(N):
            for j in range(M):
                if arr[i][j] != 0:
                    # 주변 물 개수 세기
                    tmp = 0
                    for d in range(4):
                        mx = i + dx[d]
                        my = j + dy[d]
    
                        if 0 <= mx < N and 0 <= my < M and arr[mx][my] == 0:
                            tmp += 1
    
                    if arr[i][j] - tmp >= 0:
                        temp[i][j] = arr[i][j] - tmp
                    else:
                        temp[i][j] = 0
        # 녹여놓은 배열을 다시 기존 배열에 반영
        arr = copy.deepcopy(temp)
        ans += 1

print(ans)