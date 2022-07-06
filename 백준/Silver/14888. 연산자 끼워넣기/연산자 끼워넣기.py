import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
giho = list(map(int,input().split()))
r_min = 2147000000
r_max = -2147000000
def DFS(L,sum,a,b,c,d):
    global r_max, r_min
    if L == n:
        if sum >r_max:
            r_max = sum
        if sum < r_min:
            r_min = sum
        return
    else:
        if a>0:
            DFS(L+1,sum+arr[L],a-1,b,c,d)
        if b >0:
            DFS(L+1,sum-arr[L],a,b-1,c,d)
        if c >0:
            DFS(L+1,sum*arr[L],a,b,c-1,d)
        if d >0:
            if sum <0:
                DFS(L+1,(abs(sum)//arr[L])*-1,a,b,c,d-1)
            else:
                DFS(L+1,sum//arr[L],a,b,c,d-1)
    
DFS(1,arr[0],giho[0],giho[1],giho[2],giho[3])

print(r_max)
print(r_min)