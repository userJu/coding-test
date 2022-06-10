import sys
from collections import deque
input = sys.stdin.readline
M,N = map(int,input().split())

board = []
for _ in range(N):
    board.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]
dq= deque([])

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            dq.append((i,j))


def BFS():
    while dq:
        p = dq.popleft()
        for i in range(4):
            new_x = p[0]+dx[i]
            new_y = p[1]+dy[i]
            if 0<= new_x <N and 0 <= new_y <M and board[new_x][new_y] == 0:
                dq.append((new_x,new_y))
                board[new_x][new_y] = board[p[0]][p[1]]+1
BFS()         
res = 0
for i in range(N):
    if 0 in board[i]:
        res = -1
        break
    else:
        maxValue = max(board[i])
        if maxValue>res:
            res = maxValue -1
            
print(res)