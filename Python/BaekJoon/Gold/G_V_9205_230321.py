# 9205 맥주 마시면서 걸어가기
# https://www.acmicpc.net/problem/9205
from collections import deque
def bfs(hx, hy):
    q = deque()

    # 현재 위치 추가 이때 방문 배열은 편의점만 따질것이니 방문 처리 X
    q.append((hx, hy))

    while q:
        cx, cy = q.popleft()

        # 만약 현재 위치에서 종점까지 범위 내에 갈 수 있으면 정답처리후 종료
        if abs(cx - ex) + abs(cy - ey) <= 1000:
            print('happy')
            return

        # 미방문한 편의점내에서 범위 내에 갈 수 있는지
        # 범위는 맥주 20 * 50
        for i in range(n):
            # 현재 위치와 편의점들의 위치를 거리 계산
            if not visited[i]:
                dis = abs(cx - s[i][0]) + abs(cy - s[i][1])
                if dis <= 1000:
                    q.append((s[i][0], s[i][1]))
                    visited[i] = 1

    print('sad')

T = int(input())
for tc in range(T):
    n = int(input())
    hx, hy = map(int, input().split())
    s = []
    for _ in range(n):
        i, j = map(int, input().split())
        s.append((i, j))
    ex, ey = map(int, input().split())

    visited = [0] * n
    bfs(hx, hy)