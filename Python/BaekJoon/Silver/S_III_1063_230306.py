# IM 대비
# 1063 킹
# https://www.acmicpc.net/problem/1063

dic = {'R':(1, 0), 'L':(-1, 0), 'B':(0, -1), 'T':(0, 1), 'RT':(1, 1), 'LT':(-1, 1), 'RB':(1, -1), 'LB':(-1, -1)}
board = [[0] * 8 for _ in range(8)]
q, r, N = input().split()
N = int(N)

kx = ord(q[0]) - ord('A')   # 킹의 좌표
ky = int(q[1]) - 1
rx = ord(r[0]) - ord('A')   # 돌의 좌표
ry = int(r[1]) - 1

board[kx][ky] = 1
board[rx][ry] = 2

for _ in range(N):
    m = dic.get(input())

    mx = kx + m[0]
    my = ky + m[1]

    if 0 <= mx < 8 and 0 <= my < 8:
        if board[mx][my] == 2:  # 움직인 좌표가 돌 일떄
            tx = rx + m[0]
            ty = ry + m[1]
            if 0 <= tx < 8 and 0 <= ty < 8:
                board[mx][my] = 1
                board[kx][ky] = 0
                board[tx][ty] = 2                
                rx = tx
                ry = ty
                kx = mx
                ky = my
        else:
            board[mx][my] = 1
            board[kx][ky] = 0
            kx = mx
            ky = my

print(chr(ord('A') + kx) + str(ky + 1))
print(chr(ord('A') + rx) + str(ry + 1))