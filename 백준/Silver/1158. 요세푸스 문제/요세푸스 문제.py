import sys
from collections import deque
input = sys.stdin.readline
N,K = map(int,input().split())
arr = deque([i for i in range(1,N+1)])
res = []
while arr:
    arr.rotate((K-1)*-1)
    res.append(arr.popleft())
print(f'<{", ".join(str(x) for x in res)}>')

