import sys
from collections import deque
input=sys.stdin.readline

#test cases
t=int(input())

for _ in range(t):
    n,m=map(int,input().split())
    priority=deque(map(int, input().split()))
    q=deque(range(n))
    count=0
    while q:
        if priority[q[0]]==max(priority):
            if q[0]==m:
                print(count+1)
                break
            priority[q[0]]=0
            q.popleft()
            count+=1
        else:
            q.append(q.popleft())


