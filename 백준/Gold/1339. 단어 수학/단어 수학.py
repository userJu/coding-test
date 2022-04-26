N = int(input())
dict={}
for _ in range(N):
    word = input().rstrip()
    for idx, x in enumerate(word):
        if x in dict :
            dict[x]+= int(10**(len(word)-(idx+1)))
        else:
            dict[x] = int(10**(len(word)-(idx+1)))


dict = sorted(dict.items(), key = lambda item : item[1], reverse=True)
cnt = 9
res = 0
for x in dict:
    res+=x[1]*cnt
    cnt-=1
print(res)