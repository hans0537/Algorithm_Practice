# 1967 트리의 지름
# https://www.acmicpc.net/problem/1967
def dfs(s, w):
    for ss, ww in tree[s]:
        if visited[ss] == -1:
            visited[ss] = w + ww
            dfs(ss, w + ww)


N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    p, c, d = map(int, input().split())
    tree[p].append((c, d))
    tree[c].append((p, d))

# 1번 노드에서부터 가장 먼 노드를 찾는다
visited = [-1] * (N + 1)  # 가중치의 (1번과의 거리)를 담을 배열
visited[1] = 0  # 1번 노드의 가중치는
dfs(1, 0)   # 1번 노드에서 시작

# 가정 먼 노드에서 또 다른 먼 노드를 찾으면 된다
start = visited.index(max(visited))
visited = [-1] * (N + 1)
visited[start] = 0
dfs(start, 0)

print(max(visited))