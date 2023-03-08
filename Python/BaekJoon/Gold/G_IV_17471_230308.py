# 17471 게리맨더링
# https://www.acmicpc.net/problem/17471
from itertools import combinations
from collections import deque

# 구역 탐색하면서 방문 노드개수를 리턴한다
def bfs(lst):
    s = lst[0]
    q = deque()
    visited = [0] * (N + 1)
    visited[s] = 1
    q.append(s)
    sum = 0
    while q:
        v = q.popleft()
        sum += nums[v]
        for w in adjL[v]:
            # 방문 안한 정점과 내 구역인 정점들만 방문
            if not visited[w] and w in lst:
                q.append(w)
                visited[w] = 1
    return sum, visited.count(1)

N = int(input())
nums = [0] + list(map(int, input().split()))
adjL = [[] for _ in range(N + 1)]
ans = 1e9
for i in range(1, N + 1):
    lst = list(map(int, input().split()))
    adjL[i] = (lst[1:])

# 구역을 나누기
# 1번 구역부터 n // 2만큼 구역 나누기
# 어차피 한 구역이 정해지면 나머지 구역도 정해지기 때문
for i in range(1, N//2 + 1):
    coms = combinations(range(1, N + 1), i)
    for lst in coms:
        sumA, cntA = bfs(lst)   # A구역
        sumB, cntB = bfs([i for i in range(1, N + 1) if i not in lst]) # B구역(전체에서 A구역인것 제외)
        # 방문한 노드들의 합이 전체 개수와 같으면
        if cntA + cntB == N:
            ans = min(ans, abs(sumA - sumB))

if ans == 1e9:
    print(-1)
else:
    print(ans)
