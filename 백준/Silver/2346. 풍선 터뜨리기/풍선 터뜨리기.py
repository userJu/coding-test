"""
queue의 rotate 이용
"""
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
dq = deque([])
arr = list(map(int,input().split()))
for idx, x in enumerate(arr):
    dq.append((idx+1,x))
    

while dq:
    idx,rot = dq.popleft()
    if rot >0:
        dq.rotate(-(rot-1))
    else:
        dq.rotate(-rot)
    print(idx, end=" ")
