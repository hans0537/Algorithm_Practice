# 6603 로또
# https://www.acmicpc.net/problem/6603

def dfs(idx, cnt, tlst):
    # 리스트의 첫번째 원소 즉 뽑을 숫자들의 개수를 넘어가면
    if idx > lst[0]:
        if cnt == 6:
            print(*tlst)
        return

    dfs(idx + 1, cnt + 1, tlst + [lst[idx]])
    dfs(idx + 1, cnt, tlst)
    
while True:
    lst = list(map(int, input().split()))
    # 0이 입력되면 종료
    if lst[0] == 0:
        break
        
    dfs(1, 0, [])
    print()