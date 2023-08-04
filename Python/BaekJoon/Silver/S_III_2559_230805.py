# 2559 수열

N, M = map(int, input().split())
lst = list(map(int, input().split()))

# sliding window 기법
ans = -1e9
cnt = 0
for i in range(N):
    cnt += lst[i]

    if i >= M - 1:
        ans = max(cnt, ans)
        cnt -= lst[i - M + 1]

print(ans)
