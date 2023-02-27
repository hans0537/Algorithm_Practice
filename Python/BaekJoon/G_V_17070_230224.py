# 17070 파이프 옮기기 1
# https://www.acmicpc.net/problem/17070

n = int(input())
graph = [[] for _ in range(n)]

# 0은 가로, 1은 세로, 2는 대각선
dp = [[[0] * n for _ in range(n)] for _ in range(3)]

# 그래프 정보 입력
for i in range(n):
    graph[i] = list(map(int, input().split()))

dp[0][0][1] = 1  # 첫 시작 위치

# dp를 위해서는 윗 행을 사용해야하므로 첫 행을 먼저 초기화
for i in range(2, n):
    if graph[0][i] == 0:
        dp[0][0][i] = dp[0][0][i - 1]

for r in range(1, n):
    for c in range(1, n):
        # 현재위치가 대각선인 경우
        if graph[r][c] == 0 and graph[r][c - 1] == 0 and graph[r - 1][c] == 0:
            dp[2][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]

        if graph[r][c] == 0:
            # 현재 위치가 가로인 경우
            dp[0][r][c] = dp[0][r][c - 1] + dp[2][r][c - 1]
            # 현재 위치가 세로인 경우
            dp[1][r][c] = dp[1][r - 1][c] + dp[2][r - 1][c]

print(sum(dp[i][n - 1][n - 1] for i in range(3)))
'''
# DFS 방법
# 가는 방향에 따라 모든 경우의 수 체크
def dfs(x, y, d):
    global cnt

    # N,N 에 도달했을때 경우의 수 증가후 종료
    if x == N - 1 and y == N - 1:
        cnt += 1
        return

    # 현재 방향이 가로또는 대각선 이면 가로 이동
    if d == 0 or d == 1:
        if y + 1 < N:
            if board[x][y + 1] == 0:
                # 범위 내에서 벽을 피해 가로 이동
                dfs(x, y + 1, 0)

    # 현재 방향이 세로 이고 대각선이면 세로 이동
    if d == 1 or d == 2:
        if x + 1 < N:
            if board[x + 1][y] == 0:
                dfs(x + 1, y, 2)

    # 대각선 이동
    if x + 1 < N and y + 1 < N:
        if board[x][y + 1] == 0 and board[x + 1][y] == 0 and board[x + 1][y + 1] == 0:
            dfs(x + 1, y + 1, 1)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
dfs(0, 1, 0)
print(cnt)

'''

