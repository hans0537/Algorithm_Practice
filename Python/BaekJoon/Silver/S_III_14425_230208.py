# 14425 문자열의 집합
# https://www.acmicpc.net/problem/14425

N, M = map(int, input().split())

n_set = [input() for _ in range(N)]
m_list = [input() for _ in range(M)]

cnt = 0 
for i in m_list:
    if i in n_set:
        cnt += 1

print(cnt)
