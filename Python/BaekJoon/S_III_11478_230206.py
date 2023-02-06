# 11478 서로 다른 부분 문자열의 개수
# https://www.acmicpc.net/problem/11478

s = input()

ans = []
for i in range(len(s)):
    for j in range(0, len(s) + 1):
        ans.append(s[i:j])
print(len(set(ans)) - 1)