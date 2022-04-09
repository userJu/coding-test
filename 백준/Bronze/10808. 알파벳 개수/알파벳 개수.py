import sys
word = sys.stdin.readline().strip()
calc = [0]*26
for x in word:
    calc[(ord(x)-97)] +=1
print(*calc)