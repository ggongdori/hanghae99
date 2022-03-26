import sys

input = sys.stdin.readline

#입력받기
n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

#잘못된 입력 제거
if not len(a) == n or not len(b) == n:
    print("배열의 길이가 다릅니다")
    exit(1)

#오름차순
for i in range(1, len(a)):
    temp = a[i]
    idx = i
    while idx > 0 and a[idx-1] > temp:
        a[idx] = a[idx-1]
        idx -= 1
    a[idx] = temp

#내림차순
for i in range(1, len(b)):
    temp = b[i]
    idx = i
    while idx > 0 and b[idx-1] < temp:
        b[idx] = b[idx-1]
        idx -= 1
    b[idx] = temp

print(a)
print(b)