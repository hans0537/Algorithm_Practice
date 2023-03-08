# 9663 (N-Queen)
# https://www.acmicpc.net/problem/9663

n = int(input())

# 1차원 배열로 [idx, i] 위치에 퀸을 놓을수 있다
board = [0]*n
cnt = 0

# 대각선 또는 위아래 체크
def check(idx):
    for i in range(idx):
        # 배열안의 값이 같으면 같은 열, 인덱스 차이와 값의 차이가 같으면 대각선
        if board[idx] == board[i] or abs(idx - i) == abs(board[idx] - board[i]):
            return 0
    return 1


def nQueen(idx):
    global cnt

    if idx == n:
        cnt += 1
        return
    
    # 퀸을 하나씩 놓으면서 나머지 모든 경우의 수를 체크
    # 체크하면서 가능한 경우의 수만 체크 (백트레킹)
    for i in range(n):
        board[idx] = i

        if check(idx):
            nQueen(idx + 1)

nQueen(0)
print(cnt)