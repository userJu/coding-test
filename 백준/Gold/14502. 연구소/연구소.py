import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
cnt = 0
board = [list(map(int,input().split())) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]
res = -2147000000
zero_cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            zero_cnt+=1

def BFS():
    global res
    dq = deque([])
    ch_board = [[0]*M for _ in range(N)]
    res_cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                dq.append((i,j))
                ch_board[i][j] = 1
                
    while dq:
        xx,yy = dq.popleft()
        for i in range(4):
            nx = xx+dx[i]
            ny = yy+dy[i]
            if 0<=nx<N and 0<=ny<M and ch_board[nx][ny] == 0 and board[nx][ny] == 0:
                ch_board[nx][ny] = 2
                res_cnt+=1
                dq.append((nx,ny))
    res = max(zero_cnt-res_cnt,res)

            

def DFS(cnt):
    if cnt == 3:
        BFS()
        return
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                DFS(cnt+1)
                board[i][j] = 0

DFS(0)
print(res-3)
                