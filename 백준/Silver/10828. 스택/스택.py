import sys
n = int(sys.stdin.readline())
stack=[]
for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        stack.append(cmd[1])
    elif cmd[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif cmd[0]=='size':
        print(len(stack))
    elif cmd[0]=='empty':
        if stack:
            print(0)
        else:
            print(1)
    elif cmd[0]=='top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
            
            
    