# 10828 스택
# https://www.acmicpc.net/problem/10828

N = int(input())
stack = []
for _ in range(N):
    s = input()
    if 'push' in s:
        tmp = s.split()
        stack.append(tmp[1])
    else:
        if s == 'top':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
        elif s == 'size':
            print(len(stack))
        elif s == 'pop':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())
        elif s == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)