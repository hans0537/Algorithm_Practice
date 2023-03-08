# IM 대비
# 2563 색종이
# https://www.acmicpc.net/problem/2563

N = int(input())
arr = [[0] * 100 for _ in range(100)]
for i in range(N):
    y, x = map(int, input().split())
    for j in range(x, x + 10):
        arr[j][y: y + 10] = [1] * 10

cnt = 0
for lst in arr:
    cnt += lst.count(1)

print(cnt)