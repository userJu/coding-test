import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M,N,K = map(int,input().split())

    board =[[0]*M for _ in range(N)] # 저장도 여기 => 0으로
    for _ in range(K):
        X,Y = map(int,input().split())
        board[Y][X] = 1

    dx = [-1,0,1,0]
    dy = [0,-1,0,1]


    def BFS(q,w):
        dq = deque()
        dq.append((q,w)) # 좌표로 돌기

        while dq:
            p = dq.popleft()

            for k in range(4):
                x = p[0]+dx[k]
                y = p[1]+dy[k]
                if 0<=x<N and 0<=y<M and board[x][y] == 1:
                    board[x][y] = 0
                    dq.append([x,y])
        return 1

    res = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                res+=BFS(i,j)

    print(res)
    
