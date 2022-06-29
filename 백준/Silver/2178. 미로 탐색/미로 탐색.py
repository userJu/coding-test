import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
board = [list(map(int,input().rstrip())) for _ in range(N)]
ch_board = [[0]*M for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def BFS(x,y):
    dq = deque([])
    dq.append((x,y))
    ch_board[x][y] = 1
    while dq:
        xx,yy = dq.popleft()
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            if 0<=nx<N and 0<=ny<M and board[nx][ny] == 1 and ch_board[nx][ny] == 0:
                ch_board[nx][ny] = ch_board[xx][yy]+1
                dq.append((nx,ny))
                if nx == N-1 and ny == M-1:
                    return ch_board[nx][ny]
                
            
print(BFS(0,0))

