# 16120 PPAP
# https://www.acmicpc.net/problem/16120

# 성공 코드
s = input()
stack = []
for i in range(len(s)):
    # 일단 입력 받은 문자열 하나씩 스택에 넣다가
    stack.append(s[i])
    # 스택에 4글자를 계속 확인하며 PPAP를 찾으면
    # 꺼낸후 P로 대체
    if ''.join(stack[-4:]) == 'PPAP':
        for j in range(4):
            stack.pop()
        stack.append('P')
# 만약 스택이 P만 있거나 PPAP가 있으면 성공
if stack == ['P'] or stack == ['P','P','A','P']:
    print('PPAP')
else:
    print('NP')

# # 실패 2
# # 재귀로 접근하였지만 일부 테스트케이스에서 실패...
# t = 'PPAP'
# isPPAP = False
# def check(t, i):
#     if len(t) == len(s):
#         if t == s:
#             global isPPAP
#             isPPAP = True
#         return
#     else:
#         check(t[:i] + 'PPAP' + t[i + 1:], i)
#     check(t[:i + 1] + 'PPAP' + t[i + 2:], i)
#
# check(t, 0)
# if isPPAP:
#     print(t)
# else:
#     print('NP')
#

# # 실패 1
# # 이유 : 테스트케이스만 보고 여러번 ppap 변환된거 생각 못함
# s = input()
# for i in range(len(s)):
#     t = 'PPAP'
#     tmp = t[:i] + 'PPAP' + t[i + 1:]
#     if tmp == s:
#         print('PPAP')
#         break
# else:
#     print('NP')