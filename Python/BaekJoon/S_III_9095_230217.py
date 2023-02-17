# 9095 1, 2, 3 더하기
# https://www.acmicpc.net/problem/9095

numbers = [1, 2, 3]
def subset(i):
    global cnt

    # 합이 num보다 커버리면 종료
    if sum(selected) > num:
        return

    if i == num:
        if sum(selected) == num:
            cnt += 1
        return

    for j in numbers:
        selected[i] = j
        subset(i + 1)
        selected[i] = 0
        subset(i + 1)

T = int(input())
for tc in range(T):
    num = int(input())
    selected = [0] * num
    cnt = 0
    subset(0)
    print(cnt)
