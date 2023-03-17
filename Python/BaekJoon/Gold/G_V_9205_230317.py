# 9205 맥주 마시면서 걸어가기
# https://www.acmicpc.net/problem/9205

T = int(input())
for tc in range(T):
    n = int(input())
    hx, hy = map(int, input().split())
    s = []
    for _ in range(n):
        s.append(tuple(map(int, input().split())))
    ex, ey = map(int, input().split())

    print(hx, hy)
    print(s)
    print(ex, ey)