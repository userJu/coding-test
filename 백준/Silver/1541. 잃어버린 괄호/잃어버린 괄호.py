import sys
input = sys.stdin.readline
math = input().rstrip()
math = math.split('-')
res = 0
for i in range(len(math)):
    if i == 0:
        s = math[i].split('+')
        res+=sum(map(int,s))
    else:
        s = math[i].split('+')
        res-=sum(map(int,s))
print(res)
    
    
        
    
    