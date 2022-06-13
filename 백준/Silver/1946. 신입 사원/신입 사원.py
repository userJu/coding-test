import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    p =[]
    for _ in range(N):
        s,m = map(int,input().split())
        p.append((s,m))
    p.sort()
    score = 2147000000
    res = 0
    for x in p:
        if score >=x[1]:
            res+=1
            score = x[1]
    print(res)
            
            
        
        