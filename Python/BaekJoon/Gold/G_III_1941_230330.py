# 1941 소문난 칠공주
# https://www.acmicpc.net/problem/1941
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
from collections import deque

def bfs(i, j):
    q = deque()
    v2 = [[0] * 5 for _ in range(5)]

    q.append((i, j))
    v2[i][j] = 1
    cnt = 1
    while q:
        x, y = q.popleft()

        for d in range(4):
            mx = x + dx[d]
            my = y + dy[d]

            if 0 <= mx < 5 and 0 <= my < 5 and not v2[mx][my] and visited[mx][my]:
                v2[mx][my] = 1
                q.append((mx, my))
                cnt += 1

    return cnt == 7

def check():
    for i in range(5):
        for j in range(5):
            # 이미 visited에 자리를 선택해놨기에 1들이 연결 되어 있는지 판단만 하면 됨
            if visited[i][j] == 1:
                return bfs(i, j)

# 2차원 배열을 1차원 배열로 늘려서 순열을 찾는 방법
# 5X5 이기에 25 만큼의 배열을 만들어서 25명의 학생들의 순열을 찾으면 됨
def dfs(idx, cnt, s):
    global ans
    if cnt > 7:
        return

    # 종료 조건
    if idx == 25:
        # 7명 선택하고 이다솜파가 4명 이상인 경우
        if cnt == 7 and s >= 4:
            # 자리가 붙어있는지 체크 한다.
            if check():
                ans += 1
        return


    # 해당 학생을 선택하거나
    visited[idx//5][idx%5] = 1
    # 1차원 배열의 인덱스//5 는 행 인덱스%5는 열을 의미
    dfs(idx + 1, cnt + 1, s + int(arr[idx//5][idx%5] == 'S'))
    # 선택 안하거나
    visited[idx//5][idx%5] = 0
    dfs(idx + 1, cnt, s)


arr = [list(input()) for _ in range(5)]
visited = [[0] * 5 for _ in range(5)]
ans = 0
dfs(0, 0, 0)
print(ans)
