n = int(input())

p = [0]*(n+1)
p[0] = 0
p[1] = 1

if n >1:
    for i in range(2,n+1):
        p[i] = p[i-1]+p[i-2]
    
print(p[n])