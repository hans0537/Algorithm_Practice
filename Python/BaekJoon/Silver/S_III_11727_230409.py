# 11727 2×n 타일링 2
# https://www.acmicpc.net/problem/11727

n = int(input())
dp = [0] * (n + 1)

dp[1] = 1
dp[2] = 3
