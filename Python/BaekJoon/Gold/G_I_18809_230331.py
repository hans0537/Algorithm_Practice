# 18809 Gaaaaaaaaaarden
# https://www.acmicpc.net/problem/18809
from collections import deque
from copy import deepcopy
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def is_valid(x, y):
    return 0 <= x < N and 0 <= y < M and garden[x][y] != 0

# G, R 배양액 퍼트리기
def bfs(tlist):
    q = deque()
    v = [[0] * M for _ in range(N)]

    # 가져온거 정보 넣어주기
    for i in range(len(can_place)):
        if tlist[i] == 0:
            continue
        ti, tj = can_place[i]
        q.append((ti, tj))
        v[ti][tj] = tlist[i]

    cnt = 0
    # 동일한 시간에 퍼져서 만나면 꽃이 피므로
    # 하나라도 퍼지는게 끝나면 종료
    while q:
        cx, cy = q.popleft()

        if v[cx][cy] == 10: continue

        for d in range(4):
            mx = cx + dx[d]
            my = cy + dy[d]

            if is_valid(mx, my) and v[mx][my] != 10:

                if not v[mx][my]:
                    if v[cx][cy] < 0:
                        v[mx][my] = v[cx][cy] - 1
                    else:
                        v[mx][my] = v[cx][cy] + 1
                    q.append((mx, my))
                # 가려는 곳에 값이 있으면
                else:
                    if v[cx][cy] < 0:
                        if v[mx][my] + v[cx][cy] - 1 == 0:
                            v[mx][my] = 10
                            cnt += 1
                    else:
                        if v[mx][my] + v[cx][cy] + 1 == 0:
                            v[mx][my] = 10
                            cnt += 1
    return cnt

# G, R 배양액 뿌리기 경우의 수
def dfs(n, gcnt, rcnt, tlist):
    global ans

    if n == len(can_place):
        if gcnt == G and rcnt == R:
            cnt = bfs(tlist)
            ans = max(ans, cnt)
        return

    # G 선택
    dfs(n + 1, gcnt + 1, rcnt, tlist + [1])
    # R 선택
    dfs(n + 1, gcnt, rcnt + 1, tlist + [-1])
    # 선택 X
    dfs(n + 1, gcnt, rcnt, tlist + [0])

N, M, G, R = map(int, input().split())
garden = []
can_place = []
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):
        if tmp[j] == 2:
            can_place.append((i, j))
    garden.append(tmp)

ans = 0
dfs(0, 0, 0, [])
print(ans)