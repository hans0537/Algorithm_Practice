# 13549 숨바꼭질 3
# https://www.acmicpc.net/problem/13549
from collections import deque

N, K = map(int, input().split())
dp = [0] * 100001
q = deque()
# 출발 지점 저장
q.append(N)
dp[N] = 1

while q:
    x = q.popleft()

    if x == K:
        print(dp[K] - 1)
        break

    for d in (x + 1, x - 1, x * 2):
        if 0 <= d < 100001 and not dp[d]:
            # 가중치가 0이므로 가장 먼저 탐색을 끝내 놔야 한다
            if d == x * 2:
                dp[d] = dp[x]
                q.appendleft(d)
            else:
                q.append(d)
                dp[d] = dp[x] + 1



