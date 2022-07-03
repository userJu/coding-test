import sys
input = sys.stdin.readline
word = input()
resarr = []
res = ""
for i in range(len(word)):
    if i%10 == 0 and i !=0:
        resarr.append(res)
        res = ""
        res+=word[i]
    elif i == len(word)-1:
        res+=word[i]
        resarr.append(res)
    else:
        res+=word[i]
for x in resarr:
    print(x)
    
