# 14888 (연산자 끼워넣기)
# https://www.acmicpc.net/problem/14888

n = int(input())
#숫자 리스트
nums = list(map(int,input().split()))
#연산자 리스트 (+ - * //)
add, sub, mul, div = map(int, input().split())

# 최대, 최소 초기화
mx = -1e9
mi = 1e9

# DFS 사용
def dfs(idx, tot, add, sub, mul, div):
    global mx, mi
    
    # 인덱스가 숫자 개수랑 같으면 종료
    if idx == n:
        mx = max(mx, tot)
        mi = min(mi, tot)
        return

    # 0개이면 무시
    # 모든 경우의 연산을 DFS를 통해 하면서 전역변수 mx, mi 를 바꿔주면서 마지막 max 와 min을 저장 
    if add:
        dfs(idx + 1, tot + nums[idx], add - 1, sub, mul, div)
    if sub:
        dfs(idx + 1, tot - nums[idx], add, sub - 1, mul, div)
    if mul:
        dfs(idx + 1, tot * nums[idx], add, sub, mul - 1, div)
    if div:
        dfs(idx + 1, int(tot / nums[idx]), add, sub, mul, div - 1)

dfs(1, nums[0], add, sub, mul, div)
print(mx)
print(mi)