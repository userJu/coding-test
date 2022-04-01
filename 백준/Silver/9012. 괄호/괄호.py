import sys
t = int(sys.stdin.readline())
for _ in range(t):
    isvps = sys.stdin.readline().strip()
    stack=[]
    for x in isvps:
        if x == "(":
            stack.append(x)
        else:
            if stack :
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else:
            print('YES')
        
            
        