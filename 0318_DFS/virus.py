import sys

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

def dfs(s):
    global cnt
    visited[s] = 1
    for i in graph[s]: # s=1 [2,5]
        if visited[i] == 0:#i=2 [1,3]
            dfs(i)
            cnt += 1

    return cnt

print(dfs(1))