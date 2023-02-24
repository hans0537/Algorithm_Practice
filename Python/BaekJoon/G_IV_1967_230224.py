# 1967 트리의 지름
# https://www.acmicpc.net/problem/1967

N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    p, c, d = map(int, input().split())
    tree[p].append((c, d))

print(tree)