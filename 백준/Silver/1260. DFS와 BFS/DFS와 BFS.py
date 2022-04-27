import sys
from collections import deque
input = sys.stdin.readline

N,M,V = map(int,input().split())
board = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    board[a][b] = board[b][a] = 1

def DFS(L,discovered = []):
    discovered.append(L)
    print(L, end=" ")

    if len(discovered) == N:
        return
    else:
        for i in range(len(board[L])):
            if board[L][i] == 1 and i not in discovered:
                DFS(i, discovered)
           
                
    

def BFS(L):
    discovered = [L]
    dq = deque()
    dq.append(L)
    while dq:
        p = dq.popleft()
        print(p, end=" ")
        for i in range(len(board[L])):
            if board[p][i] == 1 and i not in discovered :
                discovered.append(i)
                dq.append(i)

DFS(V) 
print()
BFS(V)
