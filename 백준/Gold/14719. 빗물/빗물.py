import sys
input = sys.stdin.readline
H,W = map(int,input().split())
arr = list(map(int,input().split()))


cnt = 0
for h in range(H):
    lt = 0
    rt = W-1
    while lt<=rt:
        if arr[lt]==0:
            lt+=1
        elif arr[rt] ==0:
            rt-=1
        if arr[lt]!=0 and arr[rt]!=0:
            break
        if lt == rt:
            break
    for x in arr[lt:rt]:
        if x == 0:
            cnt+=1
    for w in range(W):
        if arr[w]>0:
            arr[w]-=1

print(cnt)
