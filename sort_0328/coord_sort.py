import sys

input = sys.stdin.readline

N = int(input())

coord = []
for _ in range(N):
    x,y = map(int, input().split())
    coord.append((x,y))
coord.sort()
coord.sort(key = lambda x: (x[0], x[1]))

for c in coord:
    print(c[0], c[1], end = "\n")
