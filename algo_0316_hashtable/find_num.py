import sys

input = sys.stdin.readline

N = int(input())
nums_dict = {}
for _ in range(N):
    nums_dict[int(input().split())] = 1
print(nums_dict)
M = int(input())
nums_dict2 = {}
for _ in range(M):