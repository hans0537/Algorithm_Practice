# 2493 탑
# https://www.acmicpc.net/problem/2493

N = int(input())
arr = list(map(int, input().split()))
ans = [0] * N
stack = []

for i in range(N):

    while stack:
        if stack[-1][1] < arr[i]:
            stack.pop()
        else:
            ans[i] = stack[-1][0] + 1
            break

    stack.append((i, arr[i]))


print(*ans)