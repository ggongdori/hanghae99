import sys
import heapq

input = sys.stdin.readline
N = int(input())
cards = []
ans = 0
for _ in range(N):
    cards.append(int(input()))

heapq.heapify(cards)

# print(cards)

print(cards)
while len(cards) != 1:
    first = heapq.heappop(cards)
    second = heapq.heappop(cards)

    temp = first + second
    ans += temp
    heapq.heappush(cards, temp)

print(ans)