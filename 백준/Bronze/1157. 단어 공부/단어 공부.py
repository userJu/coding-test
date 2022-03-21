import sys
word = sys.stdin.readline().strip().upper()
setWord = set(word)
res = ''
cnt=0
for x in list(setWord):
    counted = word.count(x)
    if counted> cnt:
        cnt = counted
        res = x.upper()
    elif counted==cnt:
        res = '?'
print(res)