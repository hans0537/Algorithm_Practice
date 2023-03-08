# IM 대비
# 3985 롤 케이크
# https://www.acmicpc.net/problem/3985

L = int(input())
N = int(input())
cnt = [0] * (L + 1)

mx1 = mx2 = 0
t = 1
for i in range(N):
    p, k = map(int, input().split())
    if mx1 < k - p + 1:
        mx1 = k - p + 1
        a = t
    tmp = 0
    for j in range(p, k + 1):
        if not cnt[j]:
            cnt[j] = t
            tmp += 1
    if tmp > mx2:
        mx2 = tmp
        l = t
    t += 1

print(a)
print(l)