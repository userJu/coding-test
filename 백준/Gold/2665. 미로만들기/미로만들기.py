import sys
import heapq
input = sys.stdin.readline
N = int(input())
INF = 2147000000
board = [list(map(int,input().rstrip())) for _ in range(N)]
ch_board = [[INF]*N for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def dj(d,x,y):
    hq = []
    heapq.heappush(hq,(d,x,y))
    ch_board[x][y] = d
    while hq:
        dd,xx,yy = heapq.heappop(hq)
        if xx == N-1 and yy == N-1:
            print(dd)
            break
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            if 0<=nx<N and 0<=ny<N and ch_board[nx][ny]> dd+1:
                if board[nx][ny] == 0:
                    ch_board[nx][ny] = min(ch_board[nx][ny],dd+1)
                else:
                    ch_board[nx][ny] = min(ch_board[nx][ny],dd)
                heapq.heappush(hq,(ch_board[nx][ny],nx,ny))
                    
dj(0,0,0)







