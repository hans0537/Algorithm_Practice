# 2164 카드2
# https://www.acmicpc.net/problem/2164

# 데큐 사용
from collections import deque
num = int(input())
deque = deque([i for i in range(1, num + 1)])
while (len(deque) > 1):     # 데큐에 값이 하나 남을때까지
    deque.popleft()
    tmp = deque.popleft()
    deque.append(tmp)
print(deque[0])

# 원형 큐 사용
num = int(input())
# 원형 큐를 사용하기 위해 앞에 빈 공간을 생성
queue = [0] + [i for i in range(1, num + 1)]
# 숫자들을 넣었다는 가정하에 rear와 front 설정
rear = num
front = 0

while True:
    front = (front + 1) % (num + 1) # 앞에 있는 카드를 버림
    tmp = queue[front]
    
    # 만약 rear 와 front가 만나면 빈것이므로 직전에 뺀값 출력
    if rear == front:
        print(tmp)
        break
    
    # 앞에거 빼고
    front = (front + 1) % (num + 1)
    # 뒤 인덱스를 가져와
    rear = (rear + 1) % (num + 1)
    # 값 넣어주기
    queue[rear] = queue[front]




