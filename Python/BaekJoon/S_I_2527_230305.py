# IM 대비
# 2527 직사각형
# https://www.acmicpc.net/problem/2527
for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    if x2 > p1 or p2 < x1 or y2 > q1 or q2 < y1:
        ans = 'd'
    elif x2 == p1 or x1 == p2:  # 세로 검사
        if q1 == y2 or q2 == y1:
            ans = 'c'
        else:
            ans = 'b'
    elif q1 == y2 or q2 == y1:  # 세로 할때 점 검사 했으니 바로 가로 검사만
            ans = 'b'
    else:
        ans = 'a'

    print(ans)
