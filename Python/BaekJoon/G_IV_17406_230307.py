# 17406 배열 돌리기 4
# https://www.acmicpc.net/problem/17406
from itertools import permutations
import copy

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
lst = [list(map(int, input().split())) for _ in range(K)]

ans = 1e9

for p in permutations(lst, K):
    # 각각의 경우의 수 에 대해 체크 해야함으로 깊은복사
    temp = copy.deepcopy(arr)
    for r, c, k in p:
        sr, sc = r - k - 1, c - k - 1
        er, ec = r + k - 1, c + k - 1

        while True:
            if sr == er and sc == ec:
                break
            tmp = temp[sr][sc]

            # 왼쪽 시계 방향 옮기기
            for i in range(sr, er):
                temp[i][sc] = temp[i + 1][sc]

            # 아래 시계 방향 옮기기
            for i in range(sc, ec):
                temp[er][i] = temp[er][i + 1]

            # 오른쪽 시계 방향 옮기기
            for i in range(er, sr, -1):
                temp[i][ec] = temp[i - 1][ec]

            # 위 시계 방향 옮기기
            for i in range(ec, sc, -1):
                if i == sc + 1:
                    temp[sr][i] = tmp
                else:
                    temp[sr][i] = temp[sr][i - 1]

            sr += 1
            sc += 1
            er -= 1
            ec -= 1

    minV = 1e9
    for lst in temp:
        minV = min(minV, sum(lst))

    ans = min(ans, minV)

print(ans)