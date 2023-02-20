# 15828 Router
# https://www.acmicpc.net/problem/15828

# 데큐 사용
from collections import deque
num = int(input())
deque = deque()
while True:
    n = int(input())

    if n == -1:
        break

    if n == 0:
        deque.popleft()
        continue

    if len(deque) < num:
        deque.append(n)

if deque:
    print(*deque)
else:
    print('empty')

# 원형큐 사용
num = int(input())
queue = [0] * (num + 1)
# 처음 값을 넣어준다
rear = 1
front = 0
queue[rear] = int(input())
while True:
    n = int(input())
    if n == -1:
        break

    if n == 0:
        front = (front + 1) % (num + 1)
        continue

    # 꽉 찼을때
    if (rear + 1) % (num + 1) == front:
        continue

    rear = (rear + 1) % (num + 1)
    queue[rear] = n

if rear == front:
    print('empty')
else:
    if rear < front:
        print(*(queue[front + 1:] + queue[:rear + 1]))
    else:
        print(*queue[front + 1:rear + 1])


