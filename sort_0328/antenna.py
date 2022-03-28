import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0

ans = arr[(n-1)//2]

if n == 0:
    print("집이 없어요")
    exit(1)

#edge case (1, 9)
#중간값이 리스트에 없을 때
#가장 작은 집의 번호가 출력되도록

while ans > 0:
    if ans in arr:
        print(ans)
        break
    ans -= 1

