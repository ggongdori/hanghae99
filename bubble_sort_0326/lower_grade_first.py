import sys

input = sys.stdin.readline

n = int(input())


lst = []
for _ in range(n):
    name_score = input().split()
    lst.append((name_score[0], name_score[1]))

print(lst)
# lst.sort(key = lambda x: x[1])
lst.sort(reverse=True)

print(lst)
for l in lst:
    print(l[0], end = ' ')
