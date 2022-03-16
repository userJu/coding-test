import sys
n = int(sys.stdin.readline())

for _ in range(n):
    arr = list(sys.stdin.readline())
    cnt = 0
    l = 0
    for x in arr:
        if x == 'O':
            l+=1
            cnt+=l 
        else:
            l = 0           
    print(cnt)

