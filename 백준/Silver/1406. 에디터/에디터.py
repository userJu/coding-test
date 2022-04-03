import sys
stack1 = list(sys.stdin.readline().strip())
stack2=[]
m = int(sys.stdin.readline())

for _ in range(m):
    cmd = sys.stdin.readline().split()
    if cmd[0]=='P':
        stack1.append(cmd[1])
    elif cmd[0]=='L' and len(stack1)>0:
        stack2.append(stack1.pop())
    elif cmd[0] =='D' and len(stack2)>0:
        stack1.append(stack2.pop())
    elif cmd[0] == 'B' and len(stack1)>0:
        stack1.pop()
stack1.extend(reversed(stack2))
print("".join(stack1))
    
        
        

