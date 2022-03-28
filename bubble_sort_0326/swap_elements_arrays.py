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

# 하나는 오름차순, 하나는 내림차순으로 정렬
a.sort()
b.sort(reverse=True)

#k 번 반복문 돌며 값 비교,
# 무조건 바꿔야 되나?

for i in range(k):
    #값이 클 때만 바꿈
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    # a[i] >= b[i] 건너뜀
    else:
        continue

print(sum(a))

#버블 정렬 오름차순(O(N^2))
# for i in range(len(a)):
#     for j in range(len(a) - i - 1):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
#         else:
#             continue
# print(a)
#
# #버블정렬 내림차순(O(N^2))
# for i in range(len(b)):
#     for j in range(len(b) - i - 1):
#         if b[j] < b[j+1]:
#             b[j], b[j+1] = b[j+1], b[j]
#         else:
#             continue
# print(b)
