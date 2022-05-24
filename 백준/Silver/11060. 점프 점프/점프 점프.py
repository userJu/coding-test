import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
ch = [0]*N
if N == 1:
    print(0)
    sys.exit()

def BFS(x):
    dq = deque()
    dq.append(x)
    
    while dq:
        pos,jump = dq.popleft()
        for i in range(1,jump+1):
            if pos+i >=N or ch[pos+i]:
                continue
            ch[pos+i] = ch[pos] +1
            dq.append([pos+i,arr[pos+i]])
    return ch[-1] if ch[-1] else -1
print(BFS([0, arr[0]]))