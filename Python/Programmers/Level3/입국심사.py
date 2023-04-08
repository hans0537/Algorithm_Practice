def solution(n, times):
    # 시작을 1분 마지막 걸리는 시간을 n명 * 가장 오래걸리는 시간
    start, end = 1, max(times) * n

    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        # 현재 mid에 대한 시간에
        # 몇명이 심사가 가능한지 세본다.
        for i in times:
            cnt += mid // i

        # 총 심사 받을 인원보다 작으면
        if cnt < n:
            start = mid + 1
        # 시간이 충분하다면 최소값을 구해야 함으로
        else:
            end = mid - 1
    
    # start로 해야 왼쪽 값이므로 최소값이 나온다
    return start

# 답 28
print(solution(6, [7, 10]))