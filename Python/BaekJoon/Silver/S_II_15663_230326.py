# 15663 N과 M(9)
# https://www.acmicpc.net/problem/15663

def dfs(cnt, tmp):

    if cnt == M:
        print(*tmp)
        return

    # 다음 선택될때 마다 초기화
    prev = 0
    for i in range(N):
        # 현재 선택하는 단계에서 전에 골랐던게 다른 자리수에 또 있을 수 도 있으니
        # 중복 제거
        if not v[i] and lst[i] != prev:
            prev = lst[i]
            v[i] = 1
            dfs(cnt + 1, tmp + [lst[i]])
            v[i] = 0

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
v = [0] * N
dfs(0, [])
