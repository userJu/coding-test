import sys
from itertools import combinations
input = sys.stdin.readline
N,M = map(int,input().split())
res = []
def DFS(L):
    if len(res) == M:
        print(' '.join(map(str,res)))
        return
    else:
        for i in range(L,N+1):
            if i not in res:
                res.append(i)
                DFS(i+1)
                res.pop()
DFS(1)

