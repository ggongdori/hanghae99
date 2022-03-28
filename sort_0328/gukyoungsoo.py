import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

score_dict = defaultdict(list)
score_list = []
for _ in range(N):
    name, guk, young, soo = map(str, input().split())
    score_list.append([name, guk, young, soo])
for s in score_list:
    score_dict[s[0]].append([s[1], s[2], s[3]])

print(score_dict)
