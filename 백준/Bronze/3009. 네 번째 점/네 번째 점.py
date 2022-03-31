x =[] # 30 10 10 
y=[] # 20 10 20 
for _ in range(3):
    a,b = map(int, input().split())
    x.append(a)
    y.append(b)
l=0
r=0
for i in range(3):
    if x.count(x[i])==1: 
        l = x[i]
    if y.count(y[i])==1:
        r = y[i]
print(l,r)
        