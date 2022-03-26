import sys

input = sys.stdin.readline

#입력받기
n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

#잘못된 입력 제거
if not len(a) == n or not len(b) == n:
    print("배열의 길이가 다릅니다")
    exit(1) #프로그램이 에러로 인해 종료 <-> exit(0)


#오름차순
for i in range(len(a)-1):
    min_val = i
    for j in range(i + 1, len(a)):
        if a[j] < a[min_val]:
            min_val = j
    a[i], a[min_val] = a[min_val], a[i]


#내림차순
for i in range(len(b)-1):
    max_val = i  # 최솟값(min) 대신 최댓값(max)을 찾아야 함
    for j in range(i + 1, len(b)):
        if b[j] > b[max_val]:  # 부등호 방향 뒤집기
            max_val = j
    b[i], b[max_val] = b[max_val], b[i]

print(a)
print(b)
