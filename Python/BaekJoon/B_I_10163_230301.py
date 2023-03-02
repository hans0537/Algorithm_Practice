# 10163 색종이
# https://www.acmicpc.net/problem/10163

N = int(input())

arr = [[0] * 100 for _ in range(100)]

# 순서대로 색종이의 정보를 담을 변수
tmp = 1
for _ in range(N):
    y, x, w, h = map(int, input().split())
    for i in range(x, x + h):
        arr[i][y:y+w] = [tmp]*w
    tmp += 1

for i in range(1, N + 1):
    cnt = 0
    for row in arr:
        cnt += row.count(i)
    print(cnt)