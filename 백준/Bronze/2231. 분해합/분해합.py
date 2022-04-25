N = int(input())
for i in range(1,N+1):
    sum = 0
    for j in str(i):
        sum+=int(j)
    if i + sum == N:
        print(i)
        break
else:
    print(0)
    
