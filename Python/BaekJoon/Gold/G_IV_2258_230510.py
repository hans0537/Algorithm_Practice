# 2258 정육점
# https://www.acmicpc.net/problem/2258

N, M = map(int,input().split())
meats = [list(map(int, input().split())) for _ in range(N)]

# 고기의 가격은 싸고 높은 무게를 먼저 사기 위해 정렬
meats.sort(key=lambda x:x[0], reverse=True)
meats.sort(key=lambda x:x[1])

check = False
ans = 2147483647
w, s = 0, 0

for i in range(N):
    w += meats[i][0]

    # 만약 현재 고기 가격이 이전거랑 같다면
    if i > 0 and meats[i][1] == meats[i - 1][1]:
        # 이전 가격을 가져온셈 치고
        s += meats[i][1]
    else:
        # 없으면 0
        s = 0

    if M <= w:
        # 가격을 오름차순 해주었기에 현재 가격만 생각하면 된다.
        # 문제 조건에서 가격보다 싼건 덤으로 준다했기때문
        # 혹시 모를 같은 가격 더해준다
        ans = min(ans, meats[i][1] + s)
        check = True

if check:
    print(ans)
else:
    print(-1)