# 17135 캐슬 디펜스
# https://www.acmicpc.net/problem/17135

from collections import deque
#     좌 상 우 만 탐색 밑으로는 성안이기 때문에 볼 필요 없음
dx = [0, -1, 0]
dy = [-1, 0, 1]

# 궁수 배치 (DFS)
def set_anc(cnt, i):

    if i == N:
        if cnt == 3:
            print(arr[N])
            attack()
            return
        return

    if cnt == 3:
        print(arr[N])
        attack()
        return

    if arr[N][i] == 0:
        arr[N][i] = -1
        set_anc(cnt + 1, i + 1)
        arr[N][i] = 0
        set_anc(cnt, i + 1)

# 궁수 공격 (동시에 공격이므로 궁수 좌표 큐에 넣고 동시에 공격)
def attack():
    pass

# 처지한 적 수

# 적 한칸 앞으로

N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)] + [[0]*M]
set_anc(0, 0)
