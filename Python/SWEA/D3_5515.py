# 5515. 2016년 요일 맞추기 응용

# 윤년인지 입력 받는다
isLeap = input()
# 1/1 이 무슨요일인지 입력받는다
# 0 ~ 6 일 -> 토
day = int(input())
# 알고 싶은 요일을 입력받는다
m, d = map(int, input().split())

# 1 ~ 12월
date = [_ for _ in range(12)]

# 일 정의
for i in range(1, 13):
    # 29일까지 있는 경우 : 2월
    if i == 2:
        if isLeap == "leap":
            date[i - 1] = [0 for _ in range(29)]
        else:
            date[i - 1] = [0 for _ in range(28)]
    # 30일까지 있는 경우 : 4, 6, 9, 11
    elif i in [4, 6, 9, 11]:
        date[i-1] = [0 for _ in range(30)]
    # 31일까지 있는 경우 : 1, 3, 5, 7, 8, 10, 12
    else:
        date[i-1] = [0 for _ in range(31)]

for i in range(12):
    for j in range(len(date[i])):
        date[i][j] = day % 7
        day += 1

print(date[m-1][d-1])
