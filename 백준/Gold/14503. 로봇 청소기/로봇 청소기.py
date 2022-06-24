import sys
input = sys.stdin.readline
N,M = map(int,input().split())
r,c,d = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 0
# 1. 아이디어 : whlie문을 돌면서 나온 방법대로 구현한다
# 2. 시간복잡도
# 3. 자료구조
while True:
    if board[r][c]== 0 :
        board[r][c]= 2
        cnt+=1
    sw = False
    for i in range(1,5):
        nx = r + dx[d-i]
        ny = c + dy[d-i]
        if 0<=nx<N and 0<=ny<M and board[nx][ny]==0:
            r = nx
            c = ny
            d = (d-i)%4
            sw = True
            break

    # 4방향 모두 0이없는경우
    if sw == False:
        nx = r-dx[d]
        ny = c-dy[d]
        if 0<=nx<N and 0<=ny<M:
            if board[nx][ny] == 1:
                break
            else:
                r = nx
                c = ny
        else:
            break
                
print(cnt)
    
