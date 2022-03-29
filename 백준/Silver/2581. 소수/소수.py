m = int(input())
n = int(input())
arr=[]
for i in range(m,n+1):
    noPrime = 0
    if i>1:
        for j in range(2, i):
            if i % j ==0:
                noPrime +=1
                break
        if noPrime==0:
            arr.append(i)

if len(arr)>0:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)
    