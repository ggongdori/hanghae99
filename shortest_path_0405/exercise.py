import sys

input = sys.stdin.readline
INF = 1e9

v, e = map(int, input().split())
graph = [[INF] * (v+1) for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

answer = INF
for i in range(1, v+1):
    answer = min(answer, graph[i][i])

if answer == INF:
    print(-1)
else:
    print(answer)

