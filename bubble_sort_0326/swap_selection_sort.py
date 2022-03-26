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

#선택정렬
#오름차순 O(N^2)
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
for i in range(k):
    #값이 클 때만 바꿈
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        continue

print(sum(a))

#만약에 무조건 바꿔야 된다면
# for i in range(k):
#     a[i], b[i] = b[i], a[i]
#
# print(sum(a))