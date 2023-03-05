# IM 대비
# 1244 스위치 켜고 끄기
# https://www.acmicpc.net/problem/1244

N = int(input())
lst = [0] + list(map(int, input().split()))
num = int(input())
for _ in range(num):
    g, k = map(int, input().split())
    if g == 1:
        for i in range(k, N + 1, k):
            # xor 연산을 이용한 반전 시키기
            lst[i] = lst[i] ^ 1
    else:
        lst[k] = lst[k] ^ 1
        for i in range(N + 1):
            if k - i >= 1 and k + i <= N:
                if lst[k - i] == lst[k + i]:
                    lst[k - i] = lst[k - i] ^ 1
                    lst[k + i] = lst[k + i] ^ 1
                else:
                    break

for i in range(1, N + 1):
    print(lst[i], end=" ")
    if i % 20 == 0:
        print()
