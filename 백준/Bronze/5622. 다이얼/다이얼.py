import sys
n = sys.stdin.readline().strip()

alphabat = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
res=0
for x in n:
    for i in alphabat:
        if x in i :
            res+=alphabat.index(i)+3
    
print(res)
        

    