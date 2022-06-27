import sys
input = sys.stdin.readline
A,B = map(int,input().split())
INF = 2147000000
res = INF
def DFS(L,val):
    global res
    if val >B:
        return 
    if val == B:
        res = min(res,L)
        return 
    else:
        DFS(L+1, val*2)
        DFS(L+1, int(str(val)+'1'))
        
DFS(1,A)
if res ==INF:
    print(-1)
else:
    print(res)