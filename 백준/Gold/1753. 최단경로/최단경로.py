import sys
import heapq
input = sys.stdin.readline

V,E = map(int,input().split())
start = int(input())

INF = 2147000000
distance = [INF]*(V+1)

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    
def dijkstra(start):
    hq = []
    distance[start] = 0 # 시작 거리를 0으로 바꿔줌. 당연함. 시작임
    heapq.heappush(hq,(0,start)) # 거리, 노드를 차례로 놓어준다 거리가 먼저여야됨
    while hq:
        dist, now_node = heapq.heappop(hq)
        for lined_node,weight in graph[now_node]:
            cost = dist + weight # 움직이는데 드는 총비용 = 기존비용 + 새로운비용
            if cost < distance[lined_node]:
                distance[lined_node] = cost
                heapq.heappush(hq,(cost,lined_node))
dijkstra(start)

for x in distance[1:]:
    if x != INF:
        print(x)
    else:
        print('INF')
    
        
