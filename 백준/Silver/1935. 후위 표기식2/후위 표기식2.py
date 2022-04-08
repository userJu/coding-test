import sys
n = int(input())
quiz = sys.stdin.readline().strip()
stack=[]
d = dict()
for x in quiz:
    if x.isalnum() :
        if x not in d:
            d[x] = int(input())
        stack.append(d[x])
    else:
        val=0
        if x == "*":
            val = stack.pop()*stack.pop()
        elif x == "+":
            val = stack.pop()+stack.pop()
        elif x == "/":
            a = stack.pop()
            b= stack.pop()
            val = b/ a
        else:
            a = stack.pop()
            b= stack.pop()
            val = b- a
        stack.append(val)
print(f'{stack[0]:.2f}')    