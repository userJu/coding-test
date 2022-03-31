x,y,w,h = map(int,input().split())
t = abs(h-y)
r = abs(w-x)
b = y
l = x
print(min(t,r,b,l))