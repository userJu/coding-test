import sys
word = [x for x in sys.stdin.readline().rstrip()]
for i in range(len(word)):
    if word[i].isupper():
        if ord(word[i])+13 >90:
            word[i] = chr(ord(word[i])+13-26)
        else:
            word[i]= chr(ord(word[i])+13)
    elif word[i].islower():
        if ord(word[i])+13 > 122:
            word[i] = chr(ord(word[i])+13-26)
        else:
            word[i] = chr(ord(word[i])+13)
    else:
        pass
print(*word,sep="")