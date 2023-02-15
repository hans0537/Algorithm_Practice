# 9935 문자열 폭발
# https://www.acmicpc.net/problem/9935

# 스택을 활용한 문자열 처리
def bomb(s, b):
    stack = []
    # 한글자 씩 스택에 넣을때마다 폭발 문자열이 들어갔는지 확인한다.
    for i in range(len(s)):
        stack.append(s[i])
        # 스택에서 폭발 문자열 길이만큼 확인
        # 폭발문자와 같은 것을 확인하면 문자열 길이만큼 pop
        if ''.join(stack[-len(b):]) == b:
            for j in range(len(b)):
                stack.pop()

    return stack
s = input()
b = input()
lst = bomb(s, b)
print(''.join(lst)) if lst else print('FRULA')