import sys

input = sys.stdin.readline

N = int(input())
node = []
for _ in range(N-1):
    n, m = map(int, input().split())
    node.append((n, m))

print(node)