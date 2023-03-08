# 14226 이모티콘
# https://www.acmicpc.net/problem/14226

def emoticon(c, s, clip, f):
    global ans
    if c == S:
        ans = min(s, ans)
        return

    if c > S:
        return

    # 화면에 있는 이모티콘들을 클립보드에 저장
    if f:
        emoticon(c, s + 1, c, False)

    # 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
    if clip != 0:
        emoticon(c + clip, s + 1, clip, True)

    # 화면에 있는 이모티콘 중 하나를 삭제한다.
    if c > 1:
        emoticon(c - 1, s + 1, clip, True)

S = int(input())
ans = 1e9
emoticon(1, 0, 0, True)
print(ans)