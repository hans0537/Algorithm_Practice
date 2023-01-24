# 13458 (시험 감독)
# https://www.acmicpc.net/problem/13458

n = int(input())
#응시자
people = list(map(int,input().split()))
#총감독, 부감독
B, C = map(int, input().split())

# 감독관수를 담을 변수
cnt = 0
for i in people:
    i -= B
    cnt += 1
    if i > 0:
        if i % C:
            cnt += i // C + 1
        else:
            cnt += i // C

print(cnt)
