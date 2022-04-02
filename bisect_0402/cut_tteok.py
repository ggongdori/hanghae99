import sys

input = sys.stdin.readline

n, m = map(int, input().split())

tteok = list(map(int, input().split()))

start = 0
end = max(tteok)
answer = 0
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