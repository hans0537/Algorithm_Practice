# 10773 제로
# https://www.acmicpc.net/problem/10773

K = int(input())
stack = []
ans = 0
for _ in range(K):
    num = int(input())
    if num == 0:
        ans -= stack.pop()
    else:
        ans += num
        stack.append(num)

print(ans)