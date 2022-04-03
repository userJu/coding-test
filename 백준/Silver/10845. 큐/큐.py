import sys
n = int(sys.stdin.readline())
stack = []
lt = 0
for _ in range(n):
    cmd = list(sys.stdin.readline().split())
    if cmd[0]== 'push':
        stack.append(cmd[1])
    elif cmd[0] == 'pop':
        if stack:
            print(stack[0])
            stack=stack[1:]
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if stack:
            print(stack[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if stack:
            print(stack[len(stack)-1])
        else:
            print(-1)
           
        
            
        

