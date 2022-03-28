import sys

input = sys.stdin.readline

N = int(input())
coord = []

for _ in range(N):
    x, y = map(int, input().split())
    coord.append((x,y))

# print(coord)
coord.sort(key = lambda x: (x[1], x[0]))

for c in coord:
    print(c[0], c[1], end  = "\n")