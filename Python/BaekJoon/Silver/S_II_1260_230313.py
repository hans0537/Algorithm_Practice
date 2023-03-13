# 1260 DFS와 BFS
# https://www.acmicpc.net/problem/1260
from collections import deque
def bfs(s):
    q = deque([s])
    bvisited[s] = 1

    while q:
        w = q.popleft()
        bans.append(w)
        for t in adjL[w]:
            if not bvisited[t]:
                q.append(t)
                bvisited[t] = 1

def dfs(s):
    dvisited[s] = 1
    dans.append(s)
    for w in adjL[s]:
        if not dvisited[w]:
            dfs(w)

N, M, V = map(int, input().split())
adjL = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    adjL[s].append(e)
    adjL[e].append(s)

# 정렬을 해줌으로써 번호가 작은거 먼저 탐색하게 함
idx = 0
for lst in adjL:
    adjL[idx] = sorted(lst)
    idx += 1

dvisited = [0] * (N + 1)
bvisited = [0] * (N + 1)

dans = []
bans = []

dfs(V)
bfs(V)

print(*dans)
print(*bans)