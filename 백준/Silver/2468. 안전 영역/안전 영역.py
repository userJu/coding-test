import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

dx=[-1,0,1,0]
dy=[0,-1,0,1]

def BFS(x,y,k):
    dq = deque([])
    dq.append((x,y))
    new_board[x][y] = -1
    while dq:
        xx,yy = dq.popleft()
        for i in range(4):
            nx = xx+dx[i]
            ny = yy+dy[i]
            if 0<=nx<N and 0<=ny<N and board[nx][ny] > k and new_board[nx][ny] == 0:
                new_board[nx][ny] = -1
                dq.append((nx,ny))

res = -1
for k in range(101):
    cnt = 0
    new_board = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] >k and new_board[i][j]==0:
                BFS(i,j,k)
                cnt+=1
    if cnt == 0 :
        break
    res = max(res,cnt)
print(res)
                