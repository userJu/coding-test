import sys
import copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline
N = int(input())
board = [list(map(str,input().split())) for _ in range(N)]
empty = []
teachers = []

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def BFS():
    dq = deque([])
    for a,b in teachers:
        for i in range(4):
            dq.append((a,b,i))
    while dq:
        xx,yy,dd = dq.popleft()
        nx = xx+dx[dd]
        ny = yy+dy[dd]
        if 0<=nx<N and 0<=ny<N:
            if n_board[nx][ny] == 'S':
                return False
            elif n_board[nx][ny] == 'X':
                dq.append((nx,ny,dd))
    return True
                
            
for i in range(N):
    for j in range(N):
        if board[i][j] =='X':
            empty.append((i,j))
        if board[i][j] == 'T':
            teachers.append((i,j))
            
for comb in combinations(empty,3):
    n_board = copy.deepcopy(board)
    for x in comb:
        n_board[x[0]][x[1]] = 'O'
    if BFS():
        print('YES')
        break
else:
    print('NO')
        
        
        
