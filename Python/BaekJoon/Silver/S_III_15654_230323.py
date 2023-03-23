# 15654 N과 M (5)
# https://www.acmicpc.net/problem/15654

def dfs(cnt, lst):

    if cnt == M:
        print(*lst)
        return

    # 1 부터 N 까지 선택해나간다
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(cnt + 1, lst + [nums[i]])
            visited[i] = 0

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [0] * N
dfs(0, [])