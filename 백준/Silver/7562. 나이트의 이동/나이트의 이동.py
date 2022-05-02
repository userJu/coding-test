from collections import deque


# BFS 최소

dx = [-2,-2,2,2,-1,1,-1,1]
dy = [1,-1,1,-1,-2,-2,2,2]
dx = [-2,-2,2,2,-1,1,-1,1]
dy = [1,-1,1,-1,-2,-2,2,2]
def BFS(a1,a2,b1,b2):
    dq = deque()
    dq.append((a1,a2))
    board[a1][a2] = 1 
    if a1 == b1 and a2 == b2:
        return  0
    
    while dq:
        p = dq.popleft()
        cnt = 0
        
        for i in range(8):
            x = p[0] + dx[i]
            y = p[1] + dy[i]
            if 0<=x<I and 0<=y<I and board[x][y] == 0 :
                board[x][y] = 1
                ch_board[x][y] = ch_board[p[0]][p[1]]+1
                cnt+=1
                if x == b1 and y == b2:
                    return ch_board[x][y]
                dq.append((x,y))

T = int(input())
for _ in range(T):
    I = int(input()) # 한 변의 길이
    board = [[0]*I for _ in range(I)]
    ch_board = [[0]*I for _ in range(I)]
    a1,a2 = map(int,(input().split()))
    b1,b2 = map(int,(input().split()))
    print(BFS(a1,a2,b1,b2))
