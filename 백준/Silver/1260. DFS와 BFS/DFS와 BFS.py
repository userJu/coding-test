import sys
from collections import deque
input = sys.stdin.readline
N,M,V = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()
    
    
def DFS(v, visited = []):
    visited.append(v)
    print(v, end=" ")
    for i in graph[v]:
        if i not in visited:
            DFS(i,visited)

    
def BFS(v):
    dq = deque()
    dq.append(v)
    visited = []
    visited.append(v)
    while dq:
        p = dq.popleft()
        for x in graph[p]:
            if x not in visited:
                dq.append(x)
                visited.append(x)
    print(*visited)
    
DFS(V)
print()
BFS(V)
    
