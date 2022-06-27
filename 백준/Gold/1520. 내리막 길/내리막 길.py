import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
M,N = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(M)]
ch_board = [[-1]*N for _ in range(M)]

dx = [1,0,0,-1]
dy = [0,1,-1,0]

def DFS(x,y,H):
    if x == M-1 and y == N-1:
        return 1
    if ch_board[x][y] !=-1:
        return ch_board[x][y]
    ch_board[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<M and 0<=ny<N and board[nx][ny]<H:
            ch_board[x][y] += DFS(nx,ny,board[nx][ny])
    return ch_board[x][y]
                

print(DFS(0,0,board[0][0]))