# 2212 센서
# https://www.acmicpc.net/problem/2212

N = int(input())
K = int(input())

# 센서들의 좌표를 오름차순 정렬
sensors = sorted(list(map(int, input().split())))

# 각 센서들의 거리를 구한다.
dis = []
for i in range(N-1):
    dis.append((sensors[i+1] - sensors[i]))

# 센서들간의 거리를 내림차순 정렬
dis.sort(reverse=True)

# 일단 한개라고 두고 큰 거리를 순서대로 끊으면서
print(sum(dis[K-1:]))
