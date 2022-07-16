import sys
input = sys.stdin.readline
N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

ch_arr = [0]*10001
res = []
def DFS(L):
    if L == M:
        print(*res)
        return
    for x in arr:
        if ch_arr[x] == 0:
            ch_arr[x] = 1
            res.append(x)
            DFS(L+1)
            ch_arr[x] = 0
            res.pop()
DFS(0)
