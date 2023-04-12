# 각자의 조상을 찾는다
def find_set(rep, x):
    while x != rep[x]:
        x = rep[x]
    return x

# 서로 연결하여 하나의 조상으로 묶는다
def union(rep, x, y):
    rep[find_set(rep, y)] = find_set(rep, x)

def solution(n, costs):
    rep = [i for i in range(n + 1)]
    # 가중치 즉 2번째 원소를 기준으로 오름차순 정렬
    costs.sort(key=lambda x: x[2])
    # 가중치의 최소 합
    answer = 0
    for v1, v2, w in costs:
        # 조상이 같지 않으면 서로 연결이 안되어 있는거니까
        if find_set(rep, v1) != find_set(rep, v2):
            union(rep, v1, v2)
            answer += w

    return answer