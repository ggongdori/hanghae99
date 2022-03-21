import sys

input = sys.stdin.readline

#입력 받기
L, C = map(int, input().split())
chars = list(input().split())

#조건 3. 오름차순(사전식) 정렬
chars.sort()

password = []
# 내가 이 문자를 썼는지 체크
visited = [0] * C

#백트래킹 함수
def backtrack(length, start):
    #종료 조건 1+2
    #문자열 길이 L
    #모음 최소 2개, 자음 최소 1개
    if length == L:
        consonant = 0
        vowel = 0
        for word in password:
            if word in "aeiou":
                vowel += 1
            else:
                consonant += 1
        if consonant >= 2 and vowel >= 1:
            for word in password:
                print(word, end="")
            print()
        return

    #백트래킹 조건
    for i in range(start, C):
        #내가 아직 이 문자를 안 썼다면
        if visited[i] == 0:
            #썼다고 처리 해주고
            visited[i] = 1
            #암호 리스트에 추가
            password.append(chars[i])
            #재귀로 다음 문자 호출하고 하나 더 들어감
            backtrack(length + 1, i + 1)
            #백트래킹 구현
            #인덱스 0으로 만들어 하나 뒤로 돌아간 후 다음 문자 탐색
            visited[i] = 0
            password.pop()


backtrack(0, 0)
