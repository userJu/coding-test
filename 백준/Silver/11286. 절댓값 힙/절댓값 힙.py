import heapq
import sys
input = sys.stdin.readline
N = int(input())
heap=[]
for _ in range(N):
    x = int(input())
    if x != 0 :
        heapq.heappush(heap,(abs(x),x))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)

        
            
            
        