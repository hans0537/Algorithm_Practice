# 2644 촌수계산
# https://www.acmicpc.net/problem/2644
from collections import deque

def bfs(s, e):
    global ans
    q = deque([s])
    # 시작점을 방문 체크를 한후
    visited[s] = 1
    while q:
        x = q.popleft()

        if x == e:
            # 시작을 1로 했으니 1뺀후 리턴
            return visited[x] - 1

        for w in adjL[x]:
            if not visited[w]:
                visited[w] = visited[x] + 1
                q.append(w)

    # 못찾으면 -1 리턴
    return -1

# 촌수 계산은 가계도를 생각해보면 된다 즉 트리 형태의 그래프를
# 순회하여 찾으면 된다.
N = int(input())
S, E = map(int, input().split())
M = int(input())
adjL = [[] for _ in range(N + 1)]

for _ in range(M):
    p, c = map(int, input().split())
    adjL[p].append(c)
    adjL[c].append(p)

visited = [0] * (N + 1)

print(bfs(S, E))

