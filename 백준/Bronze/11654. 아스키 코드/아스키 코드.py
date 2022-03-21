import sys
n = input()
if type(n)==str:
    print(ord(n))
elif type(n)==int:
    print(chr(n))