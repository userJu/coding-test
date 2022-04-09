a,b = map(int, input().split())
large = max(a,b)
small = min(a,b)
for x in range(small+1,0,-1):
    if large%x == 0 and small%x == 0:
        print(x)
        break
calc = 1
while True:
    if (large*calc) % small ==0:
        break
    calc+=1
print(large*calc)