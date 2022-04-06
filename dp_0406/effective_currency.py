import sys

input = sys.stdin.readline

n, m = map(int, input().split())

currency = []
for _ in range(n):
    currency.append(int(input()))
dp = [10001] * (m+1)

dp[0] = 0

for i in range(n):
    for j in range(currency[i], m+1):
        if dp[j-currency[i]] != 10001:
            dp[j] = min(dp[j], dp[j-currency[i]] + 1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])



print(currency)