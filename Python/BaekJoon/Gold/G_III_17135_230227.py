# 17135 캐슬 디펜스
# https://www.acmicpc.net/problem/17135
import heapq
import copy


# 적이 더이상 없는지 확인
def checkA():
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 1:
                return False
    return True


# 궁수 배치 (DFS)
def set_anc(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i in range(0, len(arr)):
        elem = arr[i]
        rest_arr = arr[i + 1:]
        for C in set_anc(rest_arr, n - 1):
            result.append([elem] + C)

    return result


# 궁수 공격 (동시에 공격이므로 궁수 좌표 큐에 넣고 동시에 공격)
def attack(lst):
    alist = []
    # 궁수에서 가장 가까운 거리의 적을 찾
    for y in lst:
        hq = []  # 범위 내의 적들을 담을 임시 최소 힙 배열
        for i in range(N):
            for j in range(M):
                if temp[i][j] == 1:  # 적의 위치
                    dis = abs(N - i) + abs(y - j)
                    if dis <= D:
                        heapq.heappush(hq, (dis, i, j))
        if hq:
            # 거리 < 가장 왼쪽 순으로 pop이 됨
            alist.append(heapq.heappop(hq))

    cnt = 0
    for a in alist:
        d, x, y = a
        if temp[x][y] == 1:
            temp[x][y] = 0
            cnt += 1
    return cnt


# 적 한칸 앞으로
def move():
    # 앞으로 떙겨온후
    for i in range(N - 1, 0, -1):
        temp[i] = temp[i - 1]
    # 가장 1번째 줄은 0으로
    temp[0] = [0] * M


N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
anc_list = set_anc(list(range(M)), 3)
print(anc_list)
for lst in anc_list:
    tmp = 0
    temp = copy.deepcopy(arr)
    while not checkA():
        tmp += attack(lst)
        move()
    ans = max(ans, tmp)

print(ans)
