import sys
import timeit
# from itertools import combinations

input = sys.stdin.readline

#입력 받기
L, C = map(int, input().split())
chars = list(input().split())

#조건 3. 오름차순(사전식) 정렬
chars.sort()

#현재까지 탐색한 문자 보관 리스트(후보 리스트)
password = []
# 내가 이 문자를 썼는지 체크
visited = [0] * C
start_time = timeit.default_timer()  # 시작 시간 체크
#백트래킹 함수
def backtrack(length, start):
    if length == L: #종료 조건 1+2 문자열 길이 L
        consonant = 0
        vowel = 0
        for word in password:
            if word in "aeiou":
                vowel += 1
            else:
                consonant += 1
        if consonant >= 2 and vowel >= 1:  #모음 최소 2개, 자음 최소 1개
            for word in password:
                print(word, end="")
            print()
        return
    #백트래킹 반복문
    #start = 입력 문자열 중 몇 번째 문자인지
    #length = 현재까지 문자열 길이
    for i in range(start, C):
        #내가 아직 이 문자를 안 썼다면
        if visited[i] == 0:
            #썼다고 처리 해주고
            visited[i] = 1
            #암호 후보 리스트에 추가
            password.append(chars[i])
            backtrack(length + 1, i + 1)
            #백트래킹 핵심 값을 0으로 만들어 하나 뒤로 돌아간 후 다음 문자 탐색
            visited[i] = 0
            #조건에 맞지 않으면 가장 최근 문자 pop
            password.pop()
backtrack(0, 0)

# import sys
# from itertools import combinations
#
# vowels = ['a', 'e', 'i', 'o', 'u']
# L, C = map(int, sys.stdin.readline().split())
# pwd = list(map(str, sys.stdin.readline().split()))
#
# comb = combinations(pwd, L)
#
# for c in comb:
#     count = 0
#     for letter in c:
#         if letter in vowels:
#             count += 1
#
#     if (count >= 1) and (count <= L-2):
#         print(''.join(c))
terminate_time = timeit.default_timer()  # 종료 시간 체크

print("%f초 걸렸습니다." % (terminate_time - start_time))