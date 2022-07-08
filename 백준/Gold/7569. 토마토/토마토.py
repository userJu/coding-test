import sys
from collections import deque
input = sys.stdin.readline
M,N,H = map(int,input().split()) #가 세 높
board = []
dq = deque([])
for i in range(H):
    box = []
    for j in range(N):
        arr = list(map(int,input().split()))
        box.append(arr)
        for k in range(M):
            if arr[k] == 1:
                dq.append((0,i,j,k))
    board.append(box)
    box = []

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def BFS():
    restime = 0
    while dq:
        time,hh,xx,yy = dq.popleft()
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            if 0<=nx<N and 0<=ny<M and board[hh][nx][ny] == 0:
                board[hh][nx][ny] = 1
                dq.append((time+1,hh,nx,ny))
        for i in [-1,1]:
            nh = hh + i
            if 0<=nh<H and board[nh][xx][yy] == 0:
                board[nh][xx][yy] = 1
                dq.append((time+1,nh,xx,yy))
        restime = max(restime,time)

    for h in range(H):
        for i in range(N):
            for j in range(M):
                if board[h][i][j] == 0:
                    print(-1)
                    return
    print(restime)
    return
        
BFS()