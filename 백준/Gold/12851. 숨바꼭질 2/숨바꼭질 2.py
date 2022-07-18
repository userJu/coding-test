"""
BFS
"""
import sys
from collections import deque
input = sys.stdin.readline
N,K = map(int,input().split())
ch_board = [[-1,0] for _ in range(100001)]

def BFS(su):
    global time,cnt
    dq = deque([])
    dq.append(su)
    ch_board[su][0] = 0
    ch_board[su][1] = 1
    while dq:
        xx = dq.popleft()
        for nx in [xx+1,xx-1,xx*2]:
            if 0 <= nx<=100000:
                if ch_board[nx][0] == -1:
                    ch_board[nx][0] = ch_board[xx][0]+1
                    ch_board[nx][1] = ch_board[xx][1]
                    dq.append(nx)
                elif ch_board[nx][0] == ch_board[xx][0]+1:
                    ch_board[nx][1]+=ch_board[xx][1]

BFS(N)
print(ch_board[K][0])
print(ch_board[K][1])