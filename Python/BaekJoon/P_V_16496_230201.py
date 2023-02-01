# 16496 큰 수 만들기
# https://www.acmicpc.net/problem/16496
from functools import cmp_to_key
input()

# cmp_to_key는, 두 연산값들끼리의 비교를 할 때 유용하게 사용할 수 있다.
# 입력받은 원소 a, b를 ab, ba 형태로 붙여봤을 때 
# 값이 더 큰 경우에 해당하는 숫자가 앞으로 오도록 정렬 기준을 설정
nums = list(input().split())

# cmp_to_key에 줄 조건 함수 생성
def com(a, b):
    if int(a+b) < int(b+a):
        return 1
    elif int(a+b) > int(b+a):
        return -1
    return 0

arr = sorted(nums, key=cmp_to_key(com))

print(int(''.join(arr)))

