import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [1]*(n+1)
arr = []
for i in range(m):
    a,b = map(int,input().split())
    arr.append((a,b))
arr.sort()
for a,b in arr:
    if graph[b] <= graph[a]:
        graph[b] = graph[a]+1
print(*graph[1:])