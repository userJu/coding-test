import sys
import heapq

input = sys.stdin.readline
N = int(input())
minheap,maxheap = [],[]
for i in range(N):
    num = int(input())
    if len(minheap) == len(maxheap):
        heapq.heappush(maxheap,-num)
    else:
        heapq.heappush(minheap,num)
    
    if len(maxheap) >=1 and len(minheap) >=1 and maxheap[0]*-1 > minheap[0]:
        max_v = heapq.heappop(maxheap) * -1
        min_v = heapq.heappop(minheap)
        
        heapq.heappush(maxheap, min_v*-1)
        heapq.heappush(minheap, max_v)
    print(maxheap[0]*-1)
        
    
    