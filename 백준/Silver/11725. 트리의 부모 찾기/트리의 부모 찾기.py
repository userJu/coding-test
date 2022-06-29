import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]
ch_graph = [0]*(N+1)


def BFS(x):
    dq = deque([])
    dq.append(x)
    ch_graph[x] = 1
    while dq:
        p = dq.popleft()
        for x in graph[p]:
            if ch_graph[x] == 0:
                ch_graph[x] = p
                dq.append(x)


for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
BFS(1)
for x in ch_graph[2:]:
	print(x)