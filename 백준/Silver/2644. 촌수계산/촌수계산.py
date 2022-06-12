import sys
input = sys.stdin.readline

N = int(input())
a,b = map(int,input().split())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0]*(N+1)
def DFS(node):
    for x in graph[node]:
        if visited[x] == 0:
            visited[x] = visited[node]+1
            DFS(x)

DFS(a)
print(visited[b] if visited[b]>0 else -1)