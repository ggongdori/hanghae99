import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().rstrip())) for _ in range(N)]
#이번 문제에서는 사실 필요 없음(bfs에선 필요할 듯?) -> 필요함
visited = [[0]*N for _ in range(N)]


def bfs(a,b):
    q = deque()
    q.append((a,b))
    visited[a][b] = 1#방문처리
    dx = [-1,1,0,0]#상하좌우
    dy = [0,0,-1,1]
    cnt = 1 #자기 자신
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >=N:
                continue
            if visited[nx][ny] == 0: #단지가 있는데 아직 방문 안 한 경우
                visited[nx][ny] = 1 #방문처리 후
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    cnt += 1
    return cnt
ans = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            ans.append(bfs(i, j))

print(len(ans))
ans.sort()
for a in ans:
    print(a)