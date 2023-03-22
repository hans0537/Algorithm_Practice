# 1182 부분수열의 합
# https://www.acmicpc.net/problem/1182

def dfs(idx, s, cnt):
    global ans

    if idx == N:
        # 크기가 양수인 부분집합을 구함으로 cnt 체크
        if s == S and cnt > 0:
            ans += 1
        return

    dfs(idx + 1, s + lst[idx], cnt + 1)
    dfs(idx + 1, s, cnt)

N, S = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
dfs(0, 0, 0)
print(ans)