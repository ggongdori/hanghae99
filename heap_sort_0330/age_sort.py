import sys

input = sys.stdin.readline

N = int(input())
members = []

for _ in range(N):
    age, name = map(str, input().split())
    members.append((age, name))

members.sort(key=lambda x: x[0])
#나이, 입력 순으로 정렬
for m in members:
    print(m[0], m[1], end = "\n")