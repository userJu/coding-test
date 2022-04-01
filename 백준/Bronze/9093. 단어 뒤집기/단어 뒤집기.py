import sys
t = int(sys.stdin.readline())
for _ in range(t):
    case = sys.stdin.readline().split()
    res=[]
    for x in case:
        stack = []
        word=""
        for y in x:
            stack.append(y)
        while stack:
            word+=stack.pop()
        res.append(word)
    string = ' '.join(res)
    print(string)
        
