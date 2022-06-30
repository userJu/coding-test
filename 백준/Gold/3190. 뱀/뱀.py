"""
bfs?
구현
가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
다. 보드의 상하좌우 끝에 벽이 있다.

게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 
뱀은 처음에 오른쪽을 향한다.

이 게임이 몇 초에 끝나는지 계산하라.

로봇청소기
+
방향 전환 정보가 주어진다

"""
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
K = int(input())
board = [[0]*N for _ in range(N)]
dt = deque([])
for _ in range(K):
    a,b = map(int,input().split())
    board[a-1][b-1] = 2 # 사과 위치
L = int(input())
for _ in range(L):
    a,b = map(str,input().split())
    dt.append((int(a),b)) # 시작시간과 방향
    
dx = [0,1,0,-1]
dy = [1,0,-1,0]
    
def BFS(x,y):
    dq = deque([])
    dq.append((x,y))
    board[x][y] = 1
    tail = deque([])
    tail.append((x,y))
    cnt = 0
    i = 0
    while dq:
        xx,yy = dq.popleft()
        if dt and dt[0][0] == cnt:
            t,d = dt.popleft()
            if d == 'D':
                i+=1
            elif d == 'L':
                i-=1
        nx = xx+dx[i%4]
        ny = yy+dy[i%4]
        if 0<=nx<N and 0<=ny<N:
            if board[nx][ny] == 0:
                tx,ty = tail.popleft()
                board[tx][ty] = 0
                tail.append((nx,ny))
                cnt+=1    
                board[nx][ny] = 1
                dq.append((nx,ny))
            elif board[nx][ny] == 2:
                tail.append((nx,ny))
                dq.append((nx,ny))
                cnt+=1
                board[nx][ny] = 1
            elif board[nx][ny] == 1:
                cnt+=1
                break
        elif nx == N or nx <0 or ny == N or ny<0:
            cnt+=1
            break
                
    return cnt                
            
    
print(BFS(0,0))
    
    