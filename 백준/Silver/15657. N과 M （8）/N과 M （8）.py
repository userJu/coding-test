import sys
input = sys.stdin.readline
N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

res = []
def DFS(L,idx):
    if L == M:
        print(*res)
        return
    for x in arr:
        if x >= idx:
            res.append(x)
            DFS(L+1,x)
            res.pop()
DFS(0,0)