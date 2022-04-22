import heapq
import sys
N = int(input())
hq=[]
for _ in range(N):
    x = int(sys.stdin.readline())
    if x >0:
        heapq.heappush(hq, x)
    else:
        if hq:
            print(heapq.heappop(hq))
        else:
            print(0)
        
            
        