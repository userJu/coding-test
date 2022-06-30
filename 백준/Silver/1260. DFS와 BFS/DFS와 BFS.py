import sys
from collections import deque
input = sys.stdin.readline
N,M,V = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for l in graph:
    l.sort()

def DFS(x,visit =[]):
    visit.append(x)
    print(x, end=" ")
    for node in graph[x]:
        if node not in visit :
            DFS(node,visit)
def BFS(x):
    dq = deque([])
    dq.append(x)
    visit = [x]
    while dq:
        node = dq.popleft()
        for x in graph[node]:
            if x not in visit:
                visit.append(x)
                dq.append(x)
    print(*visit)
            
DFS(V)
print()
BFS(V)