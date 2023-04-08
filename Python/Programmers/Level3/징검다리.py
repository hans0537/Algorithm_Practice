def solution(distance, rocks, n):
    answer = 0

    # 정렬후 마지막 지점 넣기
    rocks.sort()
    rocks.append(distance)

    start, end = 0, distance

    while start <= end:
        # 일단 거리의 최소값을 mid라 놓는다
        mid = (start + end) // 2

        # 현재 위치, 삭제개수
        cur = 0
        del_cnt = 0
        # 거리 측정
        for i in rocks:
            # 바위 사이의 거리가 mid보다 작으면 안되므로 제거 개수 증가
            if i - cur < mid:
                del_cnt += 1
            # 아니면 현재 위치를 최신화
            else:
                cur = i

        # 만약 제거된 돌이 많으면 mid를 줄여본다
        if del_cnt > n:
            end = mid - 1
        # 돌이 적거나 같으면 최대값을 향해 찾는다
        else:
            answer = mid
            start = mid + 1

    return answer

# 답: 4
print(solution(25, [2, 14, 11, 21, 17], 2))