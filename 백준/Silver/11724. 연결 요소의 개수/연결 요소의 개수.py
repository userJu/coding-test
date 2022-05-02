import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())

graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,input().split())
    graph[u][v] = graph[v][u] = 1

visited = set()
def BFS(a):
    dq = deque()
    dq.append(a)
    visited.add(a)
    
    while dq:
        p = dq.popleft()
        for i in range(N+1):
            if graph[p][i] != 0 and i not in visited:
                dq.append(i)
                visited.add(i)
                graph[p][i] = graph[i][p] = 0

cnt = 0

for i in range(N+1):
    if i not in visited:
        cnt+=1
        BFS(i)
            
print(cnt-1)
            

