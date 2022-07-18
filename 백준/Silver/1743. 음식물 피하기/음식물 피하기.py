import sys
from collections import deque
input = sys.stdin.readline
N,M,K = map(int,input().split())
board = [[0]*M for _ in range(N)]
res = 0
for _ in range(K):
    a,b = map(int,input().split())
    board[a-1][b-1] = 1
    
dx = [-1,0,1,0]
dy = [0,-1,0,1]


def BFS(x,y):
    dq = deque([])
    dq.append((x,y))
    board[x][y] = -1
    cnt = 1
    while dq:
        xx,yy = dq.popleft()
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            if 0<=nx<N and 0<=ny<M and board[nx][ny] == 1:
                board[nx][ny] = -1
                cnt+=1
                dq.append((nx,ny))
    return cnt
        
    
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            res = max(res, BFS(i,j))
print(res)