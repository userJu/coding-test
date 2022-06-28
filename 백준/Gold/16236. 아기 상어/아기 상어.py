import sys
import heapq
from collections import deque
input = sys.stdin.readline
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]


dx = [-1,0,1,0]
dy = [0,1,0,-1]

def BFS(x,y):
    global size, cnt,res_time
    while True:
        dq = deque([])
        dq.append((x,y,0))
        ch_board = [[0]*N for _ in range(N)]
        ch_board[x][y] = 1
        hq = []
        max_time = N**2
        
        while dq:
            xx,yy,time = dq.popleft()
            if time > max_time:
                break
            for i in range(4):
                nx = xx+dx[i]
                ny = yy+dy[i]
                if 0<=nx<N and 0<=ny<N and ch_board[nx][ny] == 0 and board[nx][ny] <= size:
                    if 0< board[nx][ny]<size:
                        heapq.heappush(hq,(nx,ny,time+1))
                        max_time = time
                    dq.append((nx,ny,time+1))
                    ch_board[nx][ny] = 1
        if len(hq)>0:
            x,y,move = heapq.heappop(hq)
            res_time+=move
            cnt+=1
            board[x][y] = 0
            if cnt == size:
                cnt = 0
                size+=1
        else:
            break
                
res_time = 0
size = 2
cnt = 0    
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            board[i][j] = 0
            BFS(i,j)
            break

print(res_time)


