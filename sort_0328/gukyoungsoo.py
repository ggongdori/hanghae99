import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

score_list = []

for _ in range(n) :
    score_list.append(input().split())

score_list.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for s in score_list :
    print(s[0])
