# IM 대비
# 2567 색종이 - 2
# https://www.acmicpc.net/problem/2567

# 직전 값과 현재 값이 다르면 겉에 부분이므로 둘레 구함
def count(arr):
    cnt = 0
    for lst in arr:
        for i in range(1, len(lst)):
            if lst[i - 1] != lst[i]:
                cnt += 1
    return cnt

N = int(input())
arr = [[0] * 102 for _ in range(102)]
for i in range(N):
    y, x = map(int, input().split())
    for j in range(x, x + 10):
        arr[j][y: y + 10] = [1] * 10

# 행순회, 열순회 각각 카운트
ans = count(arr) + count(list(zip(*arr)))
print(ans)