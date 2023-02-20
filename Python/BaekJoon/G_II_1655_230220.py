import heapq
N = int(input())
res = []
lst = []
for i in range(N):
    num = int(input())
    heapq.heappush(lst, num)
    n = len(lst)

    if n % 2:
        res.append(heapq.heappop(lst))
    else:
        res.append(lst[n//2 - 1])

for i in res:
    print(i)

for i in range(N):
    num = int(input())
    lst.append(num)
    lst.sort()
    n = len(lst)

    if n % 2:
        res.append(lst[n//2])
    else:
        res.append(lst[n//2 - 1])

for i in res:
    print(i)