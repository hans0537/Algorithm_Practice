# 5014 스타트링크
# https://www.acmicpc.net/problem/5014
from collections import deque
def bfs(S):
    q = deque([S])
    visited[S] = 1

    while q:
        x = q.popleft()

        if x == G:
            print(visited[x] - 1)
            return

        # D층 내려가보고 U층 올라가본다
        for w in (x - D, x + U):
            # 만약 현재 층이 1과 F층 사이이고
            # 이전에 안가봤으면
            if 1 <= w <= F and not visited[w]:
                visited[w] = visited[x] + 1
                q.append(w)

    print('use the stairs')
    return

F, S, G, U, D = map(int, input().split())
visited = [0] * (F + 1)
bfs(S)
