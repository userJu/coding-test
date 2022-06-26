# 많은 비가 내렸을 때 물에 잠기지 않는 
# 안전한 영역이 최대로 몇 개가 만들어 지는 지를 조사하려고 한다.
# 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수

import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def BFS(x,y,k):
    dq = deque([])
    dq.append((x,y))
    ch_board[x][y] = 1
    while dq:
        xx,yy = dq.popleft()
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            if 0<=nx<N and 0<=ny<N and ch_board[nx][ny]== 0 and board[nx][ny]>k:
                ch_board[nx][ny] = 1
                dq.append((nx,ny))
                

res = 0
for k in range(101):
    ch_board = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] >k and ch_board[i][j] == 0:
                BFS(i,j,k)
                cnt+=1
    if cnt == 0:
        break
    res= max(res,cnt)
print(res)