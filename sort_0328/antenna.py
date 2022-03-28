import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0

ans = arr[(n-1)//2]

if not n == len(arr) or n == 0 or arr is None:
    print("집 번호를 입력해주세요")
    exit(1)

print(ans)
#edge case (1, 9)
#중간값이 리스트에 없을 때
#가장 작은 집의 번호가 출력되도록

# while True:
#     if ans in arr:
#         print(ans)
#         break
#     ans -= 1

