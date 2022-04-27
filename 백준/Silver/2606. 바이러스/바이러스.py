C = int(input())
N = int(input())

board=[[0]*(C+1) for _ in range(C+1)]
for _ in range(N):
    a,b = map(int,input().split())
    board[a][b] = board[b][a] = 1

visited = []
cnt = 0

def DFS(cur):
    global cnt
    visited.append(cur)
    for i in range(C+1):
        if board[cur][i] ==1 and i not in visited:
            cnt+=1
            DFS(i)
    else:
        return

DFS(1)
print(cnt)    
