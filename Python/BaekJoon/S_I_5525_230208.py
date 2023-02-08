# 5525 IOIOI
# https://www.acmicpc.net/problem/5525

n = int(input())
m = int(input())
s = input()

# 조금이라도 시간을 줄이는 방법
# IOI의 갯수만 체크해서 Pn 따라 갯수만 조정한다
i, cnt, ans = 0, 0, 0
while i < m - 1:
    if s[i:i+3] == 'IOI':
        cnt += 1
        # IOI를 찾았으니 인덱스 변경
        i += 2
        if cnt == n:
            cnt -= 1
            ans += 1
    else:
        i += 1
        cnt = 0
print(ans)


# 서브태스트 1번만 통과 
# n = int(input())
# p = 'IO' * n + 'I'
# # Pn 만들어주기
# # # I는 짝수번째 O는 홀수 번째 그리고 길이는 N + 1 + N
# # for i in range(2*n + 1):
# #     if i % 2:
# #         p += 'O'
# #     else:
# #         p += 'I'

# K = int(input())
# string = input()

# cnt = 0
# for i in range(K - 2*n + 1):
#     if string[i : i + 2*n + 1] == p:
#         cnt += 1

# print(cnt)