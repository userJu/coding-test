t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    arr=[i for i in range(1,n+1)] # 1 2 3 4 5
    for j in range(k):
        for x in range(1,n):
            arr[x]+=arr[x-1] # 1 3 6 10 15 
    print(max(arr))       

        
        
