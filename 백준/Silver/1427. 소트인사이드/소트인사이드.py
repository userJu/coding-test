import sys
input = sys.stdin.readline

n = int(input())

intarr = list(map(int,str(n)))

intarr.sort(reverse=True)

res = ''
for x in intarr:
    res+=str(x)
    
print(res)
