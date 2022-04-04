import sys
line = list(sys.stdin.readline().strip())
lt = 0 
start = 0
while lt < len(line):
    if line[lt] == '<':
        lt +=1
        while line[lt] != '>':
            lt+=1
        lt+=1
    elif line[lt].isalnum():
        start = lt
        while lt<len(line) and line[lt].isalnum():
            lt+=1
        tmp = line[start:lt]
        tmp.reverse()
        line[start:lt] = tmp
    else:
        lt+=1
print("".join(line))        