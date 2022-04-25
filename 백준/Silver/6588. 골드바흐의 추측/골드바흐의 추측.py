prime = [0]*1000002
for i in range(2,1000001):
    if prime[i] == 0:
        for j in range(2*i,1000001,i):
            prime[j] =1
        
while True :
    n = int(input())
    if n == 0 :
        break
    else:
        for i in range(2,n+1):
            if prime[i] == 0 and prime[n-i] == 0:
                print(f'{n} = {i} + {n-i}')
                break



