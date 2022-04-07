def solution(n, times):
    answer = 0
    left = min(times) * (n // 2)
    right = max(times) * n

    # right = left = 28일때 break
    while left < right:

        mid = (left + right) // 2
        # 사람 수 카운트
        cnt = 0

        for t in times:
            cnt += mid // t
        # n보다 심사할 수 있는 사람이 같거나 많으면
        if cnt >= n:
            right = mid
        # n명보다 못하면
        else:
            left = mid + 1
    answer = left

    # for i in range(1,n+1):

    return answer