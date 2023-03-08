# 2309 일곱난쟁이
# https://www.acmicpc.net/problem/2309

lst = []
for i in range(9):
    lst.append(int(input()))
lst.sort()
s = sum(lst)
for i in range(8):
    for j in range(i + 1, 9):
        if s - lst[i] - lst[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    pass
                else:
                    print(lst[k])
            exit()



