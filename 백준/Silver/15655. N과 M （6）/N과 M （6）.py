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
    for i in range(idx,N):
        res.append(arr[i])
        DFS(L+1,i+1)
        res.pop()
        
DFS(0,0)