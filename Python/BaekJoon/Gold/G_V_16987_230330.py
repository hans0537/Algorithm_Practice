# 16987 계란으로 계란치기
# https://www.acmicpc.net/problem/16987
def dfs(idx, cnt):
    global ans

    # 추가 가지치기
    # 만약 남은 계란중 깨질 계란 개수
    # 현재 깨진거 + 최대 경우의 수
    # (총 계란 - 현재 계란 번호) * 2 동시에 깨지는 경우의수
    if ans >= (cnt + (N-idx)*2):
        return

    # 종료 조건
    # 왼쪽부터 순차적으로 모든 계란을 치는 동작을 다 하면
    if idx == N:
        ans = max(ans, cnt)
        return
    
    # 만약 현재 칠 계란의 내구도가 0이 아니면
    if eggs[idx][0] > 0:
        # 계란을 들었는데 깰 계란이 없을때 확인하기 위함
        flag = False
        # 나를 제외한 모든 계란에 대해 치는 동작을 수행
        for target in range(N):
            # 안 깨진 계란을 친다
            if target != idx and eggs[target][0] > 0:
                flag = True

                eggs[target][0] -= eggs[idx][1]
                eggs[idx][0] -= eggs[target][1]
                dfs(idx + 1, cnt + int(eggs[target][0] <= 0) + int(eggs[idx][0] <= 0))
                eggs[target][0] += eggs[idx][1]
                eggs[idx][0] += eggs[target][1]

        # 만약 깰 계란이 없으면 다음 계란 집으러 ㄱ
        if not flag:
            dfs(idx + 1, cnt)
    else:
        # 현재 칠 계란이 깨진 계란이면 그냥 넘어간다
        dfs(idx + 1, cnt)

N = int(input())
eggs = [[] for _ in range(N)]
for i in range(N):
    eggs[i] = list(map(int, input().split()))

ans = 0
dfs(0, 0)
print(ans)