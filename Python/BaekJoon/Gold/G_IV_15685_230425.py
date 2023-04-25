# 15685 드래곤 커브
# https://www.acmicpc.net/problem/15685

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def bfs(i, j, d, g):
    # 현재 위치
    cx = i
    cy = j

    dlist = [d]
    # 세대 만큼 이동
    while g > 0:
        for k in range(len(dlist) - 1, -1, -1):
            arr[cx][cy] = 1

            # 방향 전환
            # 규칙에 의해 전 세대들을 거꾸로부터 1을 더한게 현재 방향
            # 방향 전환후 리스트 최신화
            cd = (dlist[k] + 1) % 4
            dlist.append(cd)

            # 현재 방향으로 한칸 이동
            mx = cx + dx[cd]
            my = cy + dy[cd]
            arr[mx][my] = 1

            # 끝점으로 최신화
            cx = mx
            cy = my

        # 세대 감소
        g -= 1


N = int(input())
arr = [[0] * 101 for _ in range(101)]

for _ in range(N):
    y, x, d, g = map(int, input().split())
    # 0세대 처리
    arr[x][y] = 1
    arr[x+dx[d]][y+dy[d]] = 1
    bfs(x+dx[d], y+dy[d], d, g)

ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
            ans += 1
print(ans)