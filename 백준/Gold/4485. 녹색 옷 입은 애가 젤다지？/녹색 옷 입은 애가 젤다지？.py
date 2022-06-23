import sys
import heapq
input = sys.stdin.readline
N = int(input())
INF = 2147000000

dx=[-1,0,1,0]
dy=[0,-1,0,1]
cnt = 0
while N!=0:
    cnt+=1
    board = [list(map(int,input().split())) for _ in range(N)]
    ch_board = [[INF]*N for _ in range(N)]

    hq = []
    heapq.heappush(hq,(board[0][0],0,0))
    ch_board[0][0] = board[0][0]
    
    while hq:
        val,x,y = heapq.heappop(hq)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx < N and 0<=ny<N and ch_board[nx][ny] == INF:
                if ch_board[nx][ny] > val+board[nx][ny]:
                    ch_board[nx][ny] = val+board[nx][ny]
                heapq.heappush(hq,(ch_board[nx][ny],nx,ny))
    print(f'Problem {cnt}: {ch_board[N-1][N-1]}')
    N = int(input())

        
    
    