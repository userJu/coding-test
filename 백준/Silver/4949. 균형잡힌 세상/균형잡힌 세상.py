while True:
    stack = []
    list = input()
    if list == '.': break
        
    for x in list:
        if x == '(':
            stack.append(x)
        elif x == ')':
            if len(stack)==0:
                stack.append(x)
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(x)
            
        elif x == '[':
            stack.append(x)
        elif x == ']':
            if len(stack)==0:
                stack.append(x)
            if stack[-1] == '[':
                stack.pop()
            else:
                stack.append(x)

    if len(stack) == 0:
        print('yes')
    else:
        print('no')
