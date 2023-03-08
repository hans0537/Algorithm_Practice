# IM 대비
# 2605 줄세우기
# https://www.acmicpc.net/problem/2605

N = int(input())
lst = list(map(int, input().split()))
res = []
num = 1
for i in lst:
    if i == 0:
        res.append(num)
        num += 1
    else:
        tmp = []
        for j in range(i):
            tmp.append(res.pop())
        res.append(num)
        while tmp:
            res.append(tmp.pop())
        num += 1

print(*res)