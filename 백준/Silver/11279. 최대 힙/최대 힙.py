import sys
import heapq
input = sys.stdin.readline

N = int(input())
hq = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if len(hq) == 0 : 
            print(0)
        else:
            print(-heapq.heappop(hq))
    else:
        heapq.heappush(hq,-x)
            
        
        
