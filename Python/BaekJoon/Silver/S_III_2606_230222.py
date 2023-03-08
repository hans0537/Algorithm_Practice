# 2606 바이러스
# https://www.acmicpc.net/problem/2606
from collections import deque

com = int(input())
link = int(input())

# 인접 리스트 생성
adjL = [[] for _ in range(com + 1)]
for i in range(link):
    x1, x2 = map(int,input().split())
    adjL[x1].append(x2)
    adjL[x2].append(x1)

# 방문 대기열 데큐 선언
q = deque()
# 방문 체크
visited = [0] * (com + 1)
# 시작 컴퓨터인 1번 컴퓨터를 대기열에 넣고 방문 처리
start = 1
q.append(start)
visited[start] = 1
cnt = 0
while q:    # 큐가 빌때까지
    # 대기열에 있는 컴퓨터들을 가져와
    x = q.popleft()

    # 연결 되어 있는 컴퓨터들을 방문하면서 감염시킨다
    for w in adjL[x]:
        if not visited[w]:
            q.append(w)
            visited[w] = 1
            cnt += 1

print(cnt)