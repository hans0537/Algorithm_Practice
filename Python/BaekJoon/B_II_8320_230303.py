# IM 대비
# 8320 직사각형을 만드는 방법
# https://www.acmicpc.net/problem/8320

N = int(input())
cnt = 0
for i in range(1, N + 1):
    # 1줄로 된 직사각형 우선 철리후
    cnt += 1
    # i가 2개 짜리부터 밑에 이어 붙여보기
    # 만약 갯수가 안넘으면 cnt 1증가
    for j in range(2, i + 1):
        if 4 <= i * j <= N:
            cnt += 1

print(cnt)