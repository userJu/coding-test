import sys
from collections import deque
input = sys.stdin.readline
N,Q = map(int,input().split())


graph = dict()
for _ in range(N-1):
    p,q,r = map(int,input().split())
    if p in graph.keys():
        graph[p].append([q,r]) 
    else:
        graph[p] = [[q,r]]
    if q in graph.keys():
        graph[q].append([p,r]) 
    else:
        graph[q] = [[p,r]]

def BFS(k,v):
    cnt = 0
    visited = [0]*(N+1)
    visited[v] = 1
    dq = deque()
    dq.append(v)
    
    while dq:
        now_video = dq.popleft()
        for next_video, usado in graph[now_video]:
            if usado >=k and visited[next_video] != 1:
                visited[next_video] = 1
                dq.append(next_video)
                cnt+=1
    return cnt
    
for _ in range(Q):
    k,v = map(int,input().split())
    print(BFS(k,v))
    
