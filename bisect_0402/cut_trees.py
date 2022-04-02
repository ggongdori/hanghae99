import sys

input = sys.stdin.readline

n, m = map(int, input().split())

trees = list(map(int, input().split()))

# print(trees)
# print(n, m)
start = 0
end = max(trees)

while start <= end:
    mid = (start+end) // 2
    tree = 0
    for t in trees:
        if t > mid:
            tree += t - mid

    if tree >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)