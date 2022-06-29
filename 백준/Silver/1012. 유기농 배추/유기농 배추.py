import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def BFS(x,y):
    dq = deque([])
    dq.append((x,y))
    board[x][y] = -1
    while dq:
        xx,yy = dq.popleft()
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            if 0<=nx<N and 0<=ny<M and board[nx][ny] == 1:
                board[nx][ny] = -1
                dq.append((nx,ny))
            
    

for _ in range(T):
    M,N,K = map(int,input().split())
    board = [[0]*M for _ in range(N)]
    for _ in range(K):
        x,y = map(int,input().split())
        board[y][x] = 1
        
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                BFS(i,j)
                cnt+=1
    print(cnt)