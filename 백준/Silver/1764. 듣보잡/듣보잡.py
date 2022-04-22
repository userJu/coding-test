N,M = map(int,input().split())
arr={} # dict 생성
res=[]
cnt=0
for i in range(N+M):
    inp = input()
    if inp in arr :
        cnt+=1
        res.append(inp)
    else:
        arr[inp]=0
res.sort()
print(cnt)
for x in res:
    print(x)