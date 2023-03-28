# 1759 암호만들기
# https://www.acmicpc.net/problem/1759

# 1번 코드
# def dfs(idx, cnt, a, b, tlst):
#     if idx == C:
#         if cnt == L and a >= 1 and b >= 2:
#             print(''.join(tlst))
#         return
#
#     if lst[idx] == 'a' or lst[idx] == 'e' or lst[idx] == 'i' or lst[idx] == 'o' or lst[idx] == 'u':
#         dfs(idx + 1, cnt + 1, a + 1, b, tlst + [lst[idx]])
#         dfs(idx + 1, cnt, a, b, tlst)
#     else:
#         dfs(idx + 1, cnt + 1, a, b + 1, tlst + [lst[idx]])
#         dfs(idx + 1, cnt, a, b, tlst)
#
# L, C = map(int, input().split())
# lst = sorted(list(input().split()))
# dfs(0, 0, 0, 0, [])

# 2번 코드
# cnt는 모음의 개수
def dfs(idx, cnt, tlst):

    # 종료 조건
    # 모음의 개수만 알아도 모든 종료조건 판별 가능
    if idx == C:
        if len(tlst) == L and cnt >= 1 and L - cnt >= 2:
            print(''.join(tlst))
        return

    dfs(idx + 1, cnt + tbl[ord(lst[idx])], tlst + [lst[idx]])
    dfs(idx + 1, cnt, tlst)

L, C = map(int, input().split())
lst = sorted(list(input().split()))
# look up table (모음인경우 1, 아닌경우 0)을 만들어 모음일때는 +1 해주기 위함
tbl = [0] * 128 # z까지 아스키값
for ch in 'aeiou':
    tbl[ord(ch)] = 1

dfs(0, 0, [])


