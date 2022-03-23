import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

#1번부터 시작하므로
node = [[] for _ in range(N+1)]
visited = [0] * (N+1)
ans = [1 for _ in range(N+1)]
for _ in range(N-1):
    n, m = map(int, input().split())
    node[n].append(m)
    node[m].append(n)

print(node)
def dfs(start):
    visited[start] = 1
    for i in node[start]:
        if visited[i] == 0:
            ans[i] = start
            dfs(i)
    return
dfs(1)

#2번 노드부터 프린트
for i in range(2, N+1):
    print(ans[i])
