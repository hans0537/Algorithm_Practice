# 11048 이동하기
# https://www.acmicpc.net/problem/11048

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):

        # 왼쪽에서 오는 경우
        if j - 1 >= 0:
            arr[i][j] = max(arr[i][j], arr[i][j] + arr[i][j - 1])

        # 위에서 오는 경우
        if i - 1 >= 0:
            arr[i][j] = max(arr[i][j], arr[i][j] + arr[i - 1][j])

        # 왼쪽 위 대각선에서 오는 경우
        if i - 1 >= 0 and j - 1 >= 0:
            arr[i][j] = max(arr[i][j], arr[i][j] + arr[i - 1][j - 1])

print(arr[N - 1][M - 1])


