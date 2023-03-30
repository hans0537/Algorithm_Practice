# 16987 계란으로 계란치기
# https://www.acmicpc.net/problem/16987
from copy import deepcopy

def dfs(idx, tmp):
    global ans

    if idx == N:
        cnt = 0
        for i in range(N):
            if tmp[i][0] <= 0:
                cnt += 1
        ans = max(ans, cnt)
        return

    if tmp[idx][0] > 0:
        for target in range(N):
            if target != idx and eggs[target][0] > 0:
                tmp[target][0] -= tmp[idx][1]
                tmp[idx][0] -= tmp[target][1]
                dfs(idx + 1, tmp)
                tmp[target][0] += tmp[idx][1]
                tmp[idx][0] += tmp[target][1]
                dfs(idx + 1, tmp)

N = int(input())
eggs = [[] for _ in range(N)]
for i in range(N):
    eggs[i] = list(map(int, input().split()))

ans = 0
dfs(0, eggs)
print(ans)