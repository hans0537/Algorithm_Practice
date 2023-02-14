# 1874 스택 수열
# https://www.acmicpc.net/problem/1874

n = int(input())
stack = []
check = True
now = 1
ans = ''
for _ in range(n):
    num = int(input())
    while now <= num:
        stack.append(now)
        ans += '+\n'
        now += 1

    if num == stack[-1]:
        stack.pop()
        ans += '-\n'
    else:
        print('NO')
        check = False
        break
if check:
    print(ans)




''' 시간 초과
n = int(input())
arr = [x for x in range(1, n + 1)]
stack = []
check = True
ans = ''
for _ in range(n):
    num = int(input())
    # 입력 받은 숫자가 스택에 없으면
    if num not in stack:
        # 기존 배열에 살아있는 숫자중 오름차순으로 스택에 넣는다
        for i in range(1, num + 1):
            if i not in arr:
                continue
            stack.append(i)
            arr.remove(i)
            # 스택에 넣었으니 + 출력
            ans += '+\n'
        # 넣었으니 가장 최근값이 num이므로 다시 pop 하고 -출력
        # 단 배열이 비었으면 (잘못된 수열 이므로) 반복문 종료
        if len(stack) == 0:
            check = False
            break
        stack.pop()
        ans += '-\n'
    # 입력 받은 숫자가 스택에 있으면 차례대로 pop해야 하므로
    elif num in stack:
        # 먼저 pop 한것이 num과 같다면 ㄱ 아니면 종료
        tmp = stack.pop()
        if tmp != num:
            check = False
            break
        ans += '-\n'

if check:
    print(ans)
else:
    print('NO')
'''
