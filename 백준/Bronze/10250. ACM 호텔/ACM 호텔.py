t = int(input())
for _ in range(t):
    h,w,n = map(int, input().split())
    if n% h == 0 :
        x = n//h
        y = h
    else:
        x = (n//h)+1
        y = n%h
    print(f'{y*100+x}')


        
    