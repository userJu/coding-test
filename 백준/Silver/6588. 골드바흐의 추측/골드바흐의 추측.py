arr=[0]*1000005
for i in range(3,int(1000000**(1/2))+1):
    if arr[i]==0:
        for x in range(2*i,1000001,i):
            arr[x]=1
while True:
    n = int(input())
    if n == 0 :
        break
    else:
        for i in range(3,n,2):
            if arr[i]==0 and arr[n-i]==0:
                print(f'{n} = {i} + {n-i}')
                break
        else: print("Goldbach's conjecture is wrong.")
        
        