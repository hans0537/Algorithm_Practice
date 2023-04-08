# 1654 랜선자르기
# https://www.acmicpc.net/problem/1654
K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]

# 1부터 가장 긴 랜선길이를 end로 놓고 시작
start, end = 1, max(arr)

while start <= end:
    mid = (start + end) // 2
    
    # 현재 mid 값으로 나눌수 있는 랜선의 수를 세본다
    tmp = 0
    for i in arr:
        tmp += i // mid

    # 만약 현재 mid값으로 개수를 센 결과가 적으면
    if N > tmp:
        end = mid - 1
    # 만약 개수보다 높으면 큰 값을 위해 계속 오른쪽 값 찾으러 간다
    else:
        start = mid + 1

# 결국 end에는 만족하는 최대값이 저장되어 있다.
print(end)