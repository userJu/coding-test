import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,0,1,0,1,-1,1,-1]
dy = [0,-1,0,1,1,-1,-1,1]



def BFS(a,b):
    dq = deque()
    dq.append((a,b))

    while dq :
        p = dq.popleft()
        for i in range(8):
            x = p[0]+dx[i]
            y = p[1]+dy[i]
            if 0<=x<h and 0 <= y < w and board[x][y] == 1:
                board[x][y] = 0
                dq.append((x,y))
    return



    


while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0 :
        break
    cnt = 0 
    board = []

    for _ in range(h):
        M = list(map(int,input().split()))
        board.append(M)

    for i in range(h):
        for j in range(w):
            if board[i][j] ==1:
                BFS(i,j)
                cnt+=1
    print(cnt)
    