import heapq # 우선순위 큐 모듈
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

gem = [list(map(int, input().split())) for _ in range(N)]
bag = [int(input()) for _ in range(K)]
# 무게가 가장 작은 가방에 무게는 작고 가장 큰 가격의 보석을 넣어야 함으로 정렬
# 가방 오름차순 정렬
bag.sort()
# 보석의 무게순으로 오름차순 정렬 (가격은 heap으로 최대값 판별할 예정)
gem.sort()


ans = 0
tmp = []
# 정렬된 가방 리스트에서 작은것부터 하나씩 가져온다
for i in bag:
    # 보석이 있고, 가방 무게에 들어갈 수 있는 보석을 판단
    while gem and i >= gem[0][0]:
        # tmp 힙 리스트에 보석이 들어갈수 있는 것들중에 
        # -를 해줌으로서 가장최소(즉 나중에 -해줄거니까 가장 비싼 보석)값을 넣어준다
        heapq.heappush(tmp, -gem[0][1])
        # gem리스트에 가장 최소값인 즉 방금전에 넣으거 빼기
        print(heapq.heappop(gem))
    # 만약 tmp 배열에 값이 있고 가방이 남았으면 가장 비싼거 부터 빼오기
    if tmp:
        ans -= heapq.heappop(tmp)

print(ans)




######## 시간 초과 코드 ###########
'''
N, K = map(int, input().split())

dic = {}
for _ in range(N):
    w, m = map(int, input().split())
    # 가격을 key값 무게를 value로 지정
    # 가격이 우선순위가 큼으로 탐색하기 쉽게 key로 지정
    dic[m] = w

# 역순으로 정렬을 하면 앞에서부터 탐색
# 즉 우선순위가 높은 가장 비싼 보석부터 탐색
s_list = sorted(dic.keys(), reverse=True)

# 가격을 누적합 할 변수
ans = 0
for _ in range(K):
    # 가방의 정보를 담을 bag
    bag = int(input())
    
    # 비싼 보석부터 정렬해둔 리스트를 하나씩 비교하여
    # 가방에 들어가면 리스트에서 pop한후 ans에 누적합하고 반복문 종료
    # 반복문 종료하는 이유는 보석 하나만 넣기 위함
    for i in range(len(s_list)):
        if bag >= dic.get(s_list[i]):
            ans += s_list.pop(i)
            break

print(ans)
'''

