import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(N+1)
def DFS(L):
    for i in graph[L]:
        if visited[i] == 0:
            visited[i] = L
            DFS(i)
DFS(1)

for i in range(2,N+1):
    print(visited[i])

    