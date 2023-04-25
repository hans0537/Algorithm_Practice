# 15685 드래곤 커브
# https://www.acmicpc.net/problem/15685

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def bfs(i, j, d, g):
    # 현재 길이
    l = 0
    # 현재 위치
    cx = i
    cy = j

    # 세대 만큼 이동
    while g > 0:
        if l == 0:
            arr[cx][cy] = 1

            # 현재 방향으로 한칸 이동
            mx = cx + dx[d]
            my = cy + dy[d]
            arr[mx][my] = 1

            # 끝점에서 시계 방향 전환
            cx = mx
            cy = my
            d = (d + 1) % 4

            l += 1
        else:
            for _ in range(l):
                arr[cx][cy] = 1

                # 현재 방향으로 한칸 이동
                mx = cx + dx[d]
                my = cy + dy[d]
                arr[mx][my] = 1

                # 끝점에서 시계 방향 전환
                cx = mx
                cy = my
                d = (d + 1) % 4

            l += l
        g -= 1


N = int(input())
arr = [[0] * 10 for _ in range(10)]

for _ in range(N):
    y, x, d, g = map(int, input().split())
    bfs(x, y, d, g)

print(arr)