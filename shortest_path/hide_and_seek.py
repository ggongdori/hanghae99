import heapq
import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

#0은 버림
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b,1)
    graph[b].append(a,1)

INF = 1e9
start = 1
distance = [INF] * (n+1)

def hide_and_seek(start):
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, node = heapq.heappop(queue)
        if dist > distance[node]:
            continue
        for n in graph[node]:
            #거리 업데이트
            cost = distance[node] + n[1]
            if cost < distance[n[0]]:
                distance[n[0]] = cost
                heapq.heappush(queue, (cost, n[0]))

    max_node = 0
    max_dist = 0
    max_node_lst = []
    for i in range(1, n+1):
        if max_dist < distance[i]:
            max_node = i
            max_dist = distance[i]
            max_node_lst = [max_node]
        elif max_dist == distance[i]:
            max_node_lst.append(i)
    print(max_node, max_dist, len(max_node_lst))

hide_and_seek(start)
