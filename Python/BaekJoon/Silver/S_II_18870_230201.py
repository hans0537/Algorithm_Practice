# 18870 좌표 압축
# https://www.acmicpc.net/problem/18870

N = int(input())
spots = list(map(int, input().split()))

# 시간초과
# for i in range(N):
#     cnt = 0
#     for j in range(N):
#         # i번째 원소보다 작고,
#         # 현재 j번째 원소가 j번째 이전에 안나왔으면 (즉 중복 제거)
#         if spots[i] > spots[j] and spots[j] not in spots[:j]:
#             cnt += 1
#     ans.append(cnt)

# 중복제거후 오름차순 정렬을 하면 인덱스가 갯수가 된다
s_list = sorted(set(spots), reverse=False)
dic = {s_list[i] : i for i in range(len(s_list))}

for i in spots:
    print(dic[i], end=" ")
