import sys
from collections import deque
input = sys.stdin.readline
N,K = map(int,input().split())
INF = 2147000000

def BFS(N,K):
    dq = deque([])
    dq.append((0,N))
    ch_board = [INF] * (100001)
    ch_board[N] = 0
    while dq:
        val, node = dq.popleft()
        for x in [(1,node+1),(1,node-1),(0,node*2)]:
            if 0<=x[1]<100001:
                if ch_board[x[1]] > val+x[0]:
                    ch_board[x[1]] = val+x[0]
                    dq.append((ch_board[x[1]],x[1]))
    return ch_board[K]

print(BFS(N,K))
                    
    
