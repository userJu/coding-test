# 우선순위 큐, heap을 이용

import sys
import heapq
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for i in range(N)]
heapq.heapify(arr)
sum = 0
while arr:
    if len(arr) == 1:
        break
    num1 = heapq.heappop(arr)
    num2 = heapq.heappop(arr)
    sum+=num1+num2
    heapq.heappush(arr,(num1 + num2))
    

print(sum)
    
    