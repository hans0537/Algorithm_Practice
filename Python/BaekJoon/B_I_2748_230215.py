# 2748 피보나치 수2
# https://www.acmicpc.net/problem/2748

# DP를 활용하여 memoization을 사용
# 일반적인 재귀를 사용하면 시간초과
def fib(n):
    f = [0] * (n + 1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i-1] + f[i-2]

    return f[n]
N = int(input())
print(fib(N))