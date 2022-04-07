def solution(triangle):
    answer = 0
    #맨 마지막 줄 [4,5,2,6,5]
    dp = [triangle[-1]]
    print(dp)
    #뒤에서 두번째 줄 부터 맨 윗 줄까지 뒤로 하나씩 탐색
    for i in range(len(triangle) - 2, -1, -1):
        #업데이트 된 값 넣을 리스트 추가
        dp.append([])
        # print(dp)
        for j in range(len(triangle[i])):
            print(dp[-2][j])
            print(dp[-2][j+1])
            print(triangle[i][j])
            dp[-1].append(max(dp[-2][j], dp[-2][j+1])+triangle[i][j])
    # print(dp)
    answer = dp[-1][0]
    return answer