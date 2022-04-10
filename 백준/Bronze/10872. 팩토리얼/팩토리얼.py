n = int(input())
res = 1
if n <2:
    print(1)
else:
    for i in range(2,n+1):
        res = res*i
    print(res)