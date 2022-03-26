a,b,c = map(int, input().split())
t = int(input())
if c + t>=60:
    b = b+((c+t)//60)
    c = (c+t)%60
    if b >=60:
        a = (a + (b//60))%24
        b = b%60
elif c+t <60:
    c = c+t
print(a,b,c)


