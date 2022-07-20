import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [1]*(n+1)
arr = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)

for i in range(1,n+1):
    for b in arr[i]:
        graph[b] = max(graph[b], graph[i]+1)
print(*graph[1:])