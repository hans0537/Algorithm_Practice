# 1911 흙길 보수하기
# https://www.acmicpc.net/problem/1911

N, L = map(int, input().split())
lst = []
for _ in range(N):
    s, e = map(int, input().split())
    lst.append((s, e))
lst.sort()

# 개수
cnt = 0
# 현재 널판지의 끝 위치
cur = 0

for s, e in lst:
    # 만약 널판지가 시작위치를 넘어버리면
    if cur > s:
        # 시작위치를 널판지 끝위치로 바꾸고 시작
        s = cur

    # 시작 위치에서 널판지를 놓으면서 끝을 넘어가면 종료
    while s < e:
        # 현재 시작 위치에서 널판지를 놓는다
        s += L
        cnt += 1
    # 넘어가면 현재 끝위치를 널판지 끝위치로 최신화
    cur = s

print(cnt)
