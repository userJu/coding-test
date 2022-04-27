import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
board = [list(map(int,input().rstrip())) for _ in range(N)]
board_cnt =  [[0]*M for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 최소의 칸 => BFS
def BFS(a,b):
    dq = deque()
    dq.append((a,b))
    board[a][b] = 0
    board_cnt[a][b] = 1
    
    while dq:
        p = dq.popleft()
        
        if p[0] == N-1 and p[1] ==M-1:
            return board_cnt[p[0]][p[1]]


        for i in range(4):
            x = p[0]+dx[i]
            y = p[1]+dy[i]
            if 0<=x<N and 0<=y < M and board[x][y] == 1:
                board[x][y] = 0
                board_cnt[x][y] = board_cnt[p[0]][p[1]]+1
                dq.append((x,y))
                
print(BFS(0,0))

    