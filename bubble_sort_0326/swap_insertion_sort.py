import sys

input = sys.stdin.readline

a = map(int, input().split())
b = map(int, input().split())

if not len(a) == n or not len(b) == n:
    print("배열의 길이가 다릅니다")
    exit(1)

