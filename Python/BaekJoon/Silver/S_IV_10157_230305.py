# IM 대비
# 10157 자리 배정
# https://www.acmicpc.net/problem/10157

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

c, r = map(int, input().split())
num = int(input())

arr = [[0] * r for _ in range(c)]
idx = 1
d = x = y = 0

while idx <= r * c:
    arr[x][y] = idx

    if idx == num:
        break

    mx = x + dx[d]
    my = y + dy[d]

    if mx < 0 or mx >= c or my < 0 or my >= r or arr[mx][my] != 0:
        d = (d + 1) % 4

    x = x + dx[d]
    y = y + dy[d]
    idx += 1

if idx != num:
    print(0)
else:
    print(x + 1, y + 1)
