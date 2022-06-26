import sys
from collections import deque
input = sys.stdin.readline
N,M,K,s = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)

dq = deque([])
dq.append(s)
ch_graph = [-1]*(N+1)
ch_graph[s] = 0

while dq:
    p = dq.popleft()
    for x in graph[p]:
        if ch_graph[x] == -1:
            dq.append(x)
            ch_graph[x] = ch_graph[p]+1
if K not in ch_graph:
    print(-1)
else:
    for idx,x in enumerate(ch_graph):
        if x == K:
            print(idx)


    