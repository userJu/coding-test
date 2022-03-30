n = int(input())
remain = n
arr=[]
while n >1: 
    for i in range(2,n+1):
        if n%i == 0 :
            arr.append(i)
            n = n//i
            break
for x in arr:
    print(x)
            
            
        