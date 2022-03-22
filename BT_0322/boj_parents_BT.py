import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

#1번부터 시작하므로
node = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(N-1):
    n, m = map(int, input().split())
    node[n].append(m)
    node[m].append(n)

def Dfs(start, node, visited):
    for i in node[start]:
        if visited[i] == 0:
            visited[i] = start
            Dfs(i, node, visited)

Dfs(1, node, visited)

for i in range(2, N+1):
    print(visited[i])
