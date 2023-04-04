# 1799 비숍
# https://www.acmicpc.net/problem/1799
def dfs(n, cnt):
    global ans

    # 현재 개수 + 현재 깊이에서 끝까지 선택한 값
    # 위의 개수가 최대값보다 안 크면 미리 종료
    if ans >= (cnt + 2*N - n) // 2:
        return

    # 배치가 끝났으면 개수 최신화
    if n >= 2*N - 1:
        ans = max(ans, cnt)
        return

    # 현재 사선 번호에서 놓을 수 있는 좌표를 탐색해서 다 가본다
    for x, y in can_place[n]:
        # 현재 위치를 놓냐
        # 만약 x - y (오른쪽 아래 대각선) 에 이미 놓여져 있지 않으면
        if not v[x - y]:
            v[x - y] = 1
            # 2개씩 증가
            dfs(n + 2, cnt + 1)
            v[x - y] = 0
    
    # 그냥 안놓고 넘어간다
    dfs(n + 2, cnt)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 사선마다 하나씩 넣어 보려한다.
# 사선번호는 (i + j)가 일정한것으로 오른쪽 위 대각선 라인에 놓을수 있는 좌표를 넣는다
can_place = [[] for _ in range(2*N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            # 인덱스를 사선 번호로, 놓을 자리를 값으로 넣어준다.
            can_place[i + j].append((i, j))

# 오른쪽 아래 대각선에 놓여있는지 판별
v = [0] * (2*N)
# 체스판의 흑/백은 비숍이 상호간 이동이 불가 (독립적)
# 흰색 검은색 따로 계산...
# 0 부터 2씩증가 + 1부터 2씩 증가
ans = 0
dfs(0, 0)   # 0부터 2씩 증가
t = ans
ans = 0
dfs(1, 0)   # 1부터 2씩 증가
print(ans + t)