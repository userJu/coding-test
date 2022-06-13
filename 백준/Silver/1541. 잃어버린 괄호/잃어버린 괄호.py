sik = input().split('-')
s = 0
for i in sik[0].split('+'):
    s +=int(i)
for i in sik[1:]:
    for j in i.split('+'):
        s-=int(j)
print(s)
        
                
        
    