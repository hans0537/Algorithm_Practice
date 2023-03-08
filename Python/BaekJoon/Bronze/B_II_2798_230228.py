# IM대비
# 2798 블랙잭II
# https://www.acmicpc.net/problem/2798

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            tmp = lst[i] + lst[j] + lst[k]
            if tmp <= M:
                ans = max(ans, tmp)
print(ans)
