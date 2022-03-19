import sys
from collections import deque

input = sys.stdin.readline

#num of computers
T = int(input())
#num of connections
C = int(input())
#T+1 0은 버림
graph = [[]*T for _ in range(T+1)]
visited = [0] * (T+1)
cnt = 0

for _ in range(C):
    c1, c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)
q = deque()
q.append(1)
#방문체크
visited[1] = 1

while q:
    temp = q.popleft()
    for i in graph[temp]:
        if not visited[i]:
            q.append(i)
            visited[i] = 1
            cnt +=1

print(cnt)