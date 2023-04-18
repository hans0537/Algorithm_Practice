# 1422 숫자의 신
# https://www.acmicpc.net/problem/1422

K, N = map(int, input().split())
nums = sorted([int(input()) for _ in range(K)], reverse=True)
nums = list(map(str, nums))

# 처음 가장 큰 수를 만들 숫자들을 넣는다
# 가장 큰수를 최대한 많이 넣고 나머지 숫자들을 하나씩 넣는다
first_num = [nums[0]] * (N - (K - 1)) + nums[1:]

for i in range(N - 1):
    for j in range(N - 1):
        if int(first_num[j] + first_num[j + 1]) < int(first_num[j + 1] + first_num[j]):
            first_num[j], first_num[j + 1] = first_num[j + 1], first_num[j]

print(''.join(first_num))

