# 18111 마인크래프트
# https://www.acmicpc.net/problem/18111

N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans_block = 0
ans_time = 1e9

# 0 ~ 256 까지 기준 블록을 완전탐색 한다.
for k in range(257):
    up = down = 0
    for i in range(N):
        for j in range(M):
            # 기준 블록보다 크면
            if k < arr[i][j]:
                # 깍을 블록 수 저장
                down += arr[i][j] - k
            else:
                # 같거나 크면 올릴 블록 수 저장
                up += k - arr[i][j]

    # 인벤토리 블록이 부족하면 continue
    if up > B + down:
        continue

    tmp = up + down * 2

    if ans_time >= tmp:
        ans_time = tmp
        ans_block = k

print(ans_time, ans_block)
