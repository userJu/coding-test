import sys
from collections import deque
input = sys.stdin.readline

def BFS():
    dq = deque()
    dq.append([0,0,1])
    visited =[[[0]*2 for _ in range(M)] for _ in range(N)]
    visited[0][0][1] = 1

    
    while dq:
        a,b,w = dq.popleft()
        if a == N-1 and b == M-1:
            return visited[a][b][w]
        for i in range(4):
            x = a+dx[i]
            y = b+dy[i]
            if 0<=x<N and 0<=y<M:
                if board[x][y] == 1 and w == 1:
                    visited[x][y][0] = visited[a][b][1]+1
                    dq.append([x,y,0])
                elif board[x][y] == 0 and visited[x][y][w] == 0:
                    visited[x][y][w] = visited[a][b][w] + 1
                    dq.append([x,y,w])
    return -1

if __name__ =="__main__":
    dx=[-1,0,1,0]
    dy = [0,-1,0,1]
    board=[]
    N,M = map(int,input().split())
    for i in range(N):
        board.append(list(map(int,input().strip())))
    print(BFS())