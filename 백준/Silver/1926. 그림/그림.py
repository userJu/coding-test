"""
그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력
 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의
 로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 
 그림의 넓이란 그림에 포함된 1의 개수이다.
"""
import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
wide = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def BFS(x,y):
    global wide
    dq = deque([])
    dq.append((x,y))
    board[x][y] = 0
    inner_wide = 1
    while dq:
        xx,yy = dq.popleft()
        for i in range(4):
            nx = xx+dx[i]
            ny = yy+dy[i]
            if 0<=nx<N and 0<=ny<M and board[nx][ny] == 1:
                board[nx][ny] = 0
                inner_wide+=1
                dq.append((nx,ny))
    wide = max(wide,inner_wide)
            
    

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            BFS(i,j)
            cnt+=1
        
print(cnt)
print(wide)