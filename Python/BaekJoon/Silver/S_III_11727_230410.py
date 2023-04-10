# 11727 2×n 타일링 2
# https://www.acmicpc.net/problem/11727

n = int(input())
dp = [0] * (n + 1)

# 초기값 설정
dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] * 2

print(dp[n] % 10007)