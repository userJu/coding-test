# DFS

C = int(input())
N = int(input())

graph = [[0]*(C+1) for _ in range(C+1)]

for _ in range(N):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

visited = []
cnt = 0

def DFS(now):
    global cnt
    visited.append(now)
    for i in range(C+1):
        if graph[now][i] == 1 and i not in visited:
            cnt+=1
            DFS(i)
    else:
        return

DFS(1)
print(cnt)
    
    
    