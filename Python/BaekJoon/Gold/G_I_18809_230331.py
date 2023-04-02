# 18809 Gaaaaaaaaaarden
# https://www.acmicpc.net/problem/18809
from collections import deque
from copy import deepcopy
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def is_valid(x, y, tlist):
    return 0 <= x < N and 0 <= y < M and tlist[x][y] != 0

# G, R 배양액 퍼트리기
def bfs(glist, rlist, tlist):
    gq = deque(glist)
    rq = deque(rlist)
    v = [[0] * M for _ in range(N)]

    # g이면 -1
    # r이면 1
    v[glist[0][0]][glist[0][1]] = -1
    v[rlist[0][0]][rlist[0][1]] = 1

    cnt = 0
    # 동일한 시간에 퍼져서 만나면 꽃이 피므로
    # 하나라도 퍼지는게 끝나면 종료
    while gq and rq:
        gx, gy = gq.popleft()
        rx, ry = rq.popleft()

        for d in range(4):
            m_gx = gx + dx[d]
            m_gy = gy + dy[d]

            if is_valid(m_gx, m_gy, tlist):
                if not v[m_gx][m_gy]:
                    v[m_gx][m_gy] = v[gx][gy] - 1
                    gq.append((m_gx, m_gy))
                elif v[m_gx][m_gy] != 10 and v[m_gx][m_gy][0] == 'r' and v[m_gx][m_gy][1] == gt + 1:
                    v[m_gx][m_gy] = 10
                    cnt += 1

        for d in range(4):
            m_rx = rx + dx[d]
            m_ry = ry + dy[d]

            if is_valid(m_rx, m_ry, tlist):
                if not v[m_rx][m_ry]:
                    v[m_rx][m_ry] = ('r', rt + 1)
                    rq.append((m_rx, m_ry, rt + 1))
                elif v[m_rx][m_ry] != 10 and v[m_rx][m_ry][0] == 'g' and v[m_rx][m_ry][1] == rt + 1:
                    v[m_rx][m_ry] = 10
                    cnt += 1

    return cnt

# G, R 배양액 뿌리기 경우의 수
def dfs(n, gcnt, rcnt, glist, rlist):
    global ans

    if n == len(can_place):
        if gcnt == 0 and rcnt == 0:
            tlist = deepcopy(garden)
            cnt = bfs(glist, rlist, tlist)
            ans = max(ans, cnt)
        return

    # G 선택
    if gcnt > 0:
        dfs(n + 1, gcnt - 1, rcnt, glist + [can_place[n]], rlist)
    # R 선택
    if rcnt > 0:
        dfs(n + 1, gcnt, rcnt - 1, glist, rlist + [can_place[n]])
    # 선택 X
    dfs(n + 1, gcnt, rcnt, glist, rlist)

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
dfs(0, G, R, [], [])
print(ans)