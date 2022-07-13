import sys
input = sys.stdin.readline
N,M = map(int,input().split())

res = []
def DFS(L):
    if L == M:
        print(*res)
        return
    for i in range(1,N+1):
        res.append(i)
        DFS(L+1)
        res.pop()
        
DFS(0)
        
        