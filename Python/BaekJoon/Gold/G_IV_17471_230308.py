# 17471 게리맨더링
# https://www.acmicpc.net/problem/17471

N = int(input())
nums = [0] + list(map(int, input().split()))
adjL = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    lst = list(map(int, input().split()))
    adjL[i] = (lst[1:])

# 구역을 나누기

# 구역 유효성 검사
lst = [[1,2,3], [4,5,6]]
for t in lst:
    for i in range(len(t)):
        print(adjL[t[i]])
        if adjL[t[i]] in t[i:]:
            continue

# 구역이 연결 되어 있는지 확인

print(nums)
print(adjL)
