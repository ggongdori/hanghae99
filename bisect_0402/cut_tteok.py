import sys

input = sys.stdin.readline

n, m = map(int, input().split())

#가지고 있는 떡 길이 입력 받기
tteok = list(map(int, input().split()))

#최소, 최대 길이 설정
start = 0
end = max(tteok)
answer = 0
#최소가 최대보다 크기 전까지
while start <= end:
    total = 0
    mid = (start+end) // 2
    for t in tteok:
        if t > mid:
            total += t - mid
    if total < m:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)