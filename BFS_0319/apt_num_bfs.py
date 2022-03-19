import sys

input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().rstrip())) for _ in range(N)]
#이번 문제에서는 사실 필요 없음
visited = [[0]*N for _ in range(N)]
ans = []
cnt = 0

def dfs(x,y):
    global cnt
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    graph[x][y] = 0
    cnt+=1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >=N:
            continue
        if graph[nx][ny] == 1:
            dfs(nx, ny)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt = 0
            dfs(i,j)
            ans.append(cnt)

print(len(ans))
ans.sort()
for a in ans:
    print(a)