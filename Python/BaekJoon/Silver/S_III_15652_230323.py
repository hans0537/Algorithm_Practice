# 15652 N과 M(4)
# https://www.acmicpc.net/problem/15652

def dfs(cnt, lst):
    
    if cnt == M:
        print(*lst[1:])
        return
    
    # 직전의 값보다 큰 것들을 탐색
    for i in range(lst[-1], N + 1):
        dfs(cnt + 1, lst + [i])


N, M = map(int, input().split())
# 1을 넣어놓고 시작
dfs(0, [1])