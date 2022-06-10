import sys
from collections import deque
input = sys.stdin.readline
M,N,K = map(int,input().split())

dx = [-1,0,1,0]
dy = [0,-1,0,1]

board = [[0]*N for _ in range(M)]

for _ in range(K):
    x1,y1,x2,y2= map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            board[i][j] = 1
            
res = []
def BFS(x,y):
    cnt = 1
    dq = deque([])
    dq.append((x,y))
    board[x][y] = cnt
    while dq:
        p = dq.popleft()
        for i in range(4):
            new_x = p[0] + dx[i]
            new_y = p[1] + dy[i]
            if 0<= new_x <M and 0<= new_y < N and board[new_x][new_y] == 0 :
                board[new_x][new_y] = 1
                cnt+=1
                dq.append((new_x,new_y))
    res.append(cnt)


for i in range(M):
    for j in range(N):
        if board[i][j] == 0 :
            BFS(i,j)


print(len(res))
res.sort()
print(*res)

