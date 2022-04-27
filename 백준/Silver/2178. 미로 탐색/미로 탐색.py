import sys
from collections import deque

N,M = map(int,input().split())
board=[]
cnt_board = [[0]*M for _ in range(N)]
for _ in range(N):
    board.append(list(map(int,input())))

dq = deque()
dq.append((0,0))

dx = [1,0,-1,0]
dy = [0,1,0,-1]


while dq:
    p = dq.popleft()
    for i in range(4):
        x = p[0]+dx[i]
        y = p[1]+dy[i]
        if 0<=x<N and 0 <=y < M and board[x][y]== 1:
            board[x][y] = 0
            cnt_board[x][y] = cnt_board[p[0]][p[1]]+1
            dq.append((x,y))

print(cnt_board[N-1][M-1]+1)
