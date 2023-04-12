# 11057 오르막 수
# https://www.acmicpc.net/problem/11057

# 현재 자리수에서 뒤에 올 수 있는 개수

# 2차원 dp 사용
# n = int(input())
# # 입력받은 자리수 만큼 배열 생성
# dp = [[1] * 10 for _ in range(n)]
# for i in range(1, n):
#     for j in range(10):
#         # 직전 행의 현재 j번쨰부터 9까지의 합을 가져온다
#         dp[i][j] = sum(dp[i-1][j:])
# print(sum(dp[n-1]) % 10007)

# # 1차원 dp 사용
# n = int(input())
# # 입력받은 자리수 만큼 배열 생성
# dp = [1] * 10
# for i in range(1, n):
#     for j in range(10):
#         dp[j] = sum(dp[j:])
# print(sum(dp) % 10007)

# 현재 자리수의 앞에 올 수 있는 개수
n = int(input())
dp = [1] * 10
for i in range(n - 1):
    for j in range(1, 10):
        dp[j] = dp[j] + dp[j - 1]

print(sum(dp) % 10007)
