import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
board = [list(map(int,input().strip())) for _ in range(N)]


dx = [-1,0,1,0]
dy = [0,-1,0,1]

def BFS(a,b):
    dq = deque()
    dq.append((a,b))
    allcnt = 0
    
    while dq:
        p = dq.popleft()

        for i in range(4):
            x = p[0]+dx[i]
            y = p[1]+dy[i]
            if 0 <= x < N and 0 <= y < N and board[x][y] == 1:
                allcnt+=1

                board[x][y] = 0 
                dq.append((x,y))
    return allcnt

cnt = 0
resArr=[]
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            cnt+=1
            resArr.append(BFS(i,j))
print(cnt)
resArr.sort()
for x in resArr:
    if x == 0:
        x = 1
    print(x)


