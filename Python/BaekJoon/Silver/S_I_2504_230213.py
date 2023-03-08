# 2504 괄호의 값
# https://www.acmicpc.net/problem/2504

# 새로운 풀이
s = input()
stack = []
answer = 0
tmp = 1

for i in range(len(s)):
    # 열리는 괄호가 계속 되면 곱해주는것 ([()]) => 결국 2 * 3 * 2 이므로
    # 해당 점수를 tmp에 계속 곱해주는것
    # 그리고 짝 맞추기 위해 stack에 열리는 괄호만 저장해준다
    if s[i] == '(':
        stack.append(s[i])
        tmp *= 2
    elif s[i] == '[':
        stack.append(s[i])
        tmp *= 3
    # 닫히는 괄호가 나오면
    elif s[i] == ')':
        # 스택이 비었거나 stack top 이 짝이 안맞으면 즉시 종료
        if not stack or stack[-1] == '[':
            answer = 0
            break
        # 만약 가장 안쪽 괄호 이면 answer를 증가 시켜준다.
        # 이전에 열리면서 계속 누적으로 값을 적용 시켰으므로
        # 여기서 한번에 더하면 나중에 나누기만 하면 된다
        if s[i - 1] == '(':
            answer += tmp
        # 그게 아니면 2를 다시 나누어 나간다.
        tmp //= 2
        stack.pop()     # 짝이 맞았으니 pop
    else:
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if s[i - 1] == '[':
            answer += tmp
        tmp //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(answer)

'''
# 런타임 에러
s = input()
stack = []
good = True
for i in s:
    # 일단 열리는 괄호는 스택에 넣는다
    if i == '(' or i == '[':
        stack.append(i)
    # 닫히는 괄호가 나오면
    elif i == ')' or i ==']':
        # 만약 스택이 비었으면 종료
        if len(stack) == 0:
            good = False
            break
        # 스택의 top 값을 뽑아 확인한다.
        tmp = stack.pop()
        # 만약 () 짝이 맞으면 그냥 2 를 스택에 넣는다
        if i == ')' and tmp == '(':
            stack.append(2)
        # 위와 같은 형식으로 3을 넣는다
        elif i == ']' and tmp == '[':
            stack.append(3)
        # 닫히는 괄호인데 숫자가 있다면
        elif i == ')' and type(tmp) == int and len(stack) != 0:
            check = stack.pop()
            num = tmp
            # 숫자가 안나올때 까지 숫자는 더해주고
            while type(check) == int and len(stack) != 0:
                num += check
                check = stack.pop()
            # 짝이 안 맞는 괄호면 실패
            if check == '[':
                good = False
                break
            # 아니면 여태 더해준 숫자들을 2를 곱해준다
            stack.append(num * 2)
        # 위와 같은 방식으로 3을 곱해주는 경우
        elif i == ']' and type(tmp) == int and len(stack) != 0:
            check = stack.pop()
            num = tmp
            while type(check) == int and len(stack) != 0:
                num += check
                check = stack.pop()
            if check == '(':
                good = False
                break
            stack.append(num * 3)
        # 위 모든 경우가 아니면 걍 실패
        else:
            good = False
            break
# 숫자들이 남아 있을수도 있으니 남은 것들은 더해준다
if good:
    print(sum(stack))
else:
    print(0)
'''