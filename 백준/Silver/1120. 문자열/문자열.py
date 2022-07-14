import sys
input = sys.stdin.readline
A,B = map(str,input().split())

res = 2147000000
for i in range(len(B)-len(A)+1):
    cnt = 0
    for j in range(len(A)):
        if A[j] != B[i+j]:
            cnt+=1
    res = min(res,cnt)
print(res)
