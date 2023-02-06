import heapq # 우선순위 큐 모듈

N, K = map(int, input().split())

# minheap큐 생성
# 빈 리스트를 생성한 후 heapq의 함수를 호출할 때마다 
# jem (heap) 에 요소 추가
jem = [list(map(int, input().split())) for _ in range(N)]
print(jem)
heapq.heapify(jem)
print(jem)
# for _ in range(N):
#     heapq.heappush(jem, list(map(int, input().split())))

bag = [int(input()) for _ in range(K)]
# 무게가 가장 작은 가방에 가장 큰 가격의 보석을 넣어야 함으로 정렬
bag.sort()

ans = 0
tmp = []
for i in bag:
    while jem and i >= jem[0][0]:
        heapq.heappush(tmp, -heapq.heappop(jem)[1])
    
    if tmp:
        ans -= heapq.heappop(tmp)
    elif not jem:
        break

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

