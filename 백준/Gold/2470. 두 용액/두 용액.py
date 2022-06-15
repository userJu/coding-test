import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
res = 2147000000
reslt = 0
resrt = 0
lt = 0
rt = n-1

while lt < rt:
    if abs(arr[lt]+arr[rt]) < res:
        res = abs(arr[lt]+arr[rt])
        reslt = arr[lt]
        resrt = arr[rt]
    if arr[lt]+arr[rt]<0:
        lt+=1
    elif arr[lt]+arr[rt]>0:
        rt-=1
    elif arr[lt]+arr[rt] == 0:
        break
print(reslt,resrt)

