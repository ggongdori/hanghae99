import sys

input = sys.stdin.readline

N = int(input())
word_list = []

for _ in range(N):
    word_list.append(input().rstrip())

word_list = list(set(word_list))

# print(word_list)
word_list.sort()
word_list.sort(key = len)

for w in word_list:
    print(w)