# 12851 숨바꼭질 2
# https://www.acmicpc.net/problem/12851
from collections import deque

N, K = map(int, input().split())
dp = [0] * 100001

q = deque()
q.append(N)
dp[N] = 1
cnt = 0
while q:
    x = q.popleft()

    if x == K:
        cnt += 1

    for d in (x * 2, x + 1, x - 1):
        # 최소값과 같은 횟수로 갔으면 대기열에 추가
        if 0 <= d < len(dp) and (not dp[d] or dp[d] == dp[x] + 1):
            dp[d] = dp[x] + 1
            q.append(d)

print(dp[K] - 1, cnt)
