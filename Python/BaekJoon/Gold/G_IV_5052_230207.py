# 5052 전화번호 목록
# https://www.acmicpc.net/problem/5052
import sys
input = sys.stdin.readline

T = int(input())
check = False

for tc in range(1, T + 1):
    N = int(input())
    
    numbers = [str(input().strip()) for _ in range(N)]
    numbers.sort()
    
    for i in range(N-1):
        if str(numbers[i + 1]).startswith(str(numbers[i])):
            print('NO')
            check = True
            break
    
    if check == False:
        print('YES')
    check = False