import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
INF = 2147000000
graph = [[INF]*n for _ in range(n)]

for _ in range(m):
    a,b,c = map(int,input().split())
    if graph[a-1][b-1] > c:
        graph[a-1][b-1] = c
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j :
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
            
for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            graph[i][j] = 0
    print(*graph[i])
        
    
