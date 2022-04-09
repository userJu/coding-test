import sys
while True:
    try:
        row,up, num, blank = 0,0,0,0
        string = input()
        for x in string:
            if x.islower():
                row+=1
            elif x.isupper():
                up+=1
            elif x.isdigit():
                num+=1
            elif x == " ":
                blank+=1
        print(row, up, num, blank) 
    except EOFError:
        break
   