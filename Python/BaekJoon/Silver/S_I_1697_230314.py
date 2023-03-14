# 1697 숨바꼭질
# https://www.acmicpc.net/problem/1697
from collections import deque

def bfs():
    q = deque([N])

    while q:
        x = q.popleft()
        if x == K:
            print(visited[x])
            break

        # bfs 선입선출 큐를 활용하여 가장 먼저 된 숫자를
        # 되기전 숫자의 횟수를 더해서 최소값을 유지한다
        # 방문 체크는 최소값 유지 하기 위함
        for i in (x - 1, x + 1, 2*x):
            if 0 <= i <= max_v and not visited[i]:
                visited[i] = visited[x] + 1
                q.append(i)


N, K = map(int, input().split())
max_v = 100000 # 최대값을 주어서 무한 반복 하지 않게 하기 위함
visited = [0] * (max_v + 1)
bfs()

