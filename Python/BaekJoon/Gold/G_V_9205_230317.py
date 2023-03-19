# 9205 맥주 마시면서 걸어가기
# https://www.acmicpc.net/problem/9205
import heapq

T = int(input())
for tc in range(T):
    n = int(input())
    hx, hy = map(int, input().split())
    s = []
    for _ in range(n):
        i, j = map(int, input().split())
        heapq.heappush(s, (abs(hx-i) + abs(hy-j), i, j))
    ex, ey = map(int, input().split())

    for i in range(len(s)):
        print(heapq.heappop(s))