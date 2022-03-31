def isPrime(x):
    if x ==1:
        return False
    for j in range(2,int(x**0.5)+1):
        if x % j == 0 :
            return False
    return True

limit = list(range(2,246912))
res=[]
for x in limit:
    if isPrime(x):
        res.append(x)
        
while True:
    cnt=0
    n = int(input())
    if n == 0 :
        break
    for y in res:
        if n< y <=2*n:
            cnt+=1
    print(cnt)
    
        
        
    