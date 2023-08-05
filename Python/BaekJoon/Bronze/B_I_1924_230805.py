# 2007년 요일 맞추기

# 0 ~ 6 일 -> 토
week = {
    0: "SUN",
    1: "MON",
    2: "TUE",
    3: "WED",
    4: "THU",
    5: "FRI",
    6: "SAT",
}
# 알고 싶은 요일을 입력받는다
m, d = map(int, input().split())

# 1 ~ 12월
date = [_ for _ in range(12)]

# 일 정의
for i in range(1, 13):
    if i == 2:
        date[i - 1] = [0 for _ in range(28)]
    # 30일까지 있는 경우 : 4, 6, 9, 11
    elif i in [4, 6, 9, 11]:
        date[i - 1] = [0 for _ in range(30)]
    # 31일까지 있는 경우 : 1, 3, 5, 7, 8, 10, 12
    else:
        date[i - 1] = [0 for _ in range(31)]

day = 1
for i in range(12):
    for j in range(len(date[i])):
        date[i][j] = day % 7
        day += 1

print(week[date[m - 1][d - 1]])
