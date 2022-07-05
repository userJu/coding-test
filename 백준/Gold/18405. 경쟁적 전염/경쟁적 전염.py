"""
번호 낮은 바이러스부터 증식
"""
import sys
import heapq
N,K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
S,X,Y = map(int,input().split())

dx = [-1,0,1,0]
dy = [0,-1,0,1]

hq = []
for i in range(N):
    for j in range(N):
        if board[i][j] !=0:
            heapq.heappush(hq,(0,board[i][j],i,j))

def BFS():
    while hq:
        t,v,x,y = heapq.heappop(hq)
        if t >= S:
            print(board[X-1][Y-1])
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and board[nx][ny] == 0:
                board[nx][ny] = v
                heapq.heappush(hq,(t+1,v,nx,ny))
    if t < S:
        print(board[X-1][Y-1])

BFS()
            