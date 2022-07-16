import sys
input = sys.stdin.readline
N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

res = []
def DFS(L):
    if L == M:
        print(*res)
        return
    for x in arr:
        res.append(x)
        DFS(L+1)
        res.pop()
DFS(0)
        