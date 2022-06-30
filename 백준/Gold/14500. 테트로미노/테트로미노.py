"""
bfs?
테트로미노 하나를 적절히 놓아서 
테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램
종이에 숫자가 있다.

시간복잡도
4보다 크고 500보다 작으면 N^3승까지 돌릴 수 있다.
"""

import sys
input = sys.stdin.readline
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]


def DFS(x,y,L,total):
    global res
    if res >= total + max_pos*(4-L):
        return # 예외처리
    if L == 4:
        res = max(res,total)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and visit[nx][ny] == 0:
                if L == 2:
                    visit[nx][ny] = 1
                    DFS(x,y,L+1,total+board[nx][ny])
                    visit[nx][ny] = 0
                visit[nx][ny] = 1
                DFS(nx,ny,L+1,total+board[nx][ny])
                visit[nx][ny] = 0
            
max_pos = max(map(max,board))
res = 0
for i in range(N):
    for j in range(M):
        visit[i][j] = 1
        DFS(i,j,1,board[i][j])
        visit[i][j] = 0
print(res)
