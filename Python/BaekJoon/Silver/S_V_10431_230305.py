# IM 대비
# 10431 줄세우기
# https://www.acmicpc.net/problem/10431

T = int(input())
for tc in range(1, T + 1):
    lst = list(map(int, input().split()))
    
    # 버블 정렬 방식
    cnt = 0
    for i in range(len(lst) - 1, 0, -1):
        for j in range(1, i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                cnt += 1

    print(lst[0], cnt)