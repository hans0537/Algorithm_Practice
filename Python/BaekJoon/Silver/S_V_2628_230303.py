# IM 대비
# 2628 종이자르기
# https://www.acmicpc.net/problem/2628

c, r = map(int, input().split())
N = int(input())

row = []
col = []
for i in range(N):
    d, num = map(int, input().split())
    if d == 0:
        row.append(num)
    else:
        col.append(num)

row.sort()
col.sort()

rmx = cmx = 0
tmp = 0
for i in range(r + 1):
    if i in row:
        rmx = max(rmx, i - tmp)
        tmp = i
    elif i == r:
        rmx = max(rmx, i - tmp)
        
tmp = 0
for i in range(c + 1):
    if i in col:
        cmx = max(cmx, i - tmp)
        tmp = i
    elif i == c:
        cmx = max(cmx, i - tmp)

print(rmx*cmx)

