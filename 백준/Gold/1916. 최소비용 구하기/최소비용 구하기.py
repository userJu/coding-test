import sys
import heapq
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
distance = [2147000000] *(N+1)
for i in range(M):
    a,b,p = map(int,input().split())
    graph[a].append((b,p))
    
def dj(start):
    hq = []
    heapq.heappush(hq,(0,start))
    distance[start] = 0
    while hq:
        price,now = heapq.heappop(hq)
        if price > distance[now]:
            continue
        for next_node, spend in graph[now]:
            if price+spend < distance[next_node]:
                distance[next_node] = price+spend
                heapq.heappush(hq,(distance[next_node], next_node))
    
A,B = map(int,input().split())
dj(A)
print(distance[B])