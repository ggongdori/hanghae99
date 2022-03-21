from itertools import combinations
import sys

input = sys.stdin.readline

#입력 받기
L, C = map(int, input().split())
chars = list(input().split())

vowel = set('aeiou')
chars.sort()

comb = (combinations(chars, L))

for c in comb:
    cnt = 0
    for i in comb:
        if i in vowel:
            cnt += 1
    if cnt >= 1 and cnt <= L - 2:
        print(''.join(c))

print(len(c))
print(c)
