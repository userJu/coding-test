"""
상하좌우
우리는 흰 옷 w
단지번호붙이기
가로세로 조심
"""
import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
board = [list(map(str,input().rstrip())) for _ in range(M)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def BFS(team,x,y):
    dq = deque([])
    dq.append((x,y))
    board[x][y] = 0
    cnt = 1
    while dq:
        xx,yy = dq.popleft()
        for i in range(4):
            nx = xx+dx[i]
            ny = yy+dy[i]
            if 0<=nx<M and 0<=ny<N and board[nx][ny] == team:
                board[nx][ny] = 0
                dq.append((nx,ny))
                cnt+=1
    return cnt
w_res = 0
b_res = 0
for i in range(M):
    for j in range(N):
        if board[i][j] == 'W':
            w_res +=BFS('W',i,j)**2
        elif board[i][j] == 'B':
            b_res +=BFS('B',i,j)**2
print(w_res,b_res)
            
