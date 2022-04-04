#bfs using queue

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        from collections import deque, defaultdict
        t = [0] + [float("inf")] * n
        graph = defaultdict(list)
        queue = deque([(0, k)])
        for u, v, w in times:
            graph[u].append((v, w))
        while queue:
            time, node = queue.popleft()
            if time < t[node]:
                t[node] = time
                for v, w in graph[node]:
                    queue.append((time + w, v))
        mx = max(t)
        return mx if mx < float("inf") else -1