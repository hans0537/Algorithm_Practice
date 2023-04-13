# 10844 쉬운 계단 수
# https://www.acmicpc.net/problem/10844

n = int(input())
# n = 1일때 0은 계단 수가 아님으로 0
# 나머지는 1로 초기화
dp = [0] + [1] * 9

# n = 1 부터
for _ in range(n - 1):
    tmp = [0] * 10
    for i in range(10):
        # 0번째는 1번째 거만 더하기
        if i == 0:
            tmp[i] = dp[i + 1]
        # 9번째는 8번째 거만 더하기
        elif i == 9:
            tmp[i] = dp[i - 1]
        # 나머지는 앞 뒤의 경우의수 더하기
        else:
            tmp[i] = dp[i - 1] + dp[i + 1]
    dp = tmp

print((sum(dp)) % 1000000000)