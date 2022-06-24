import sys
input = sys.stdin.readline
for _ in range(3):
    res = sum(list(map(int,input().split())))
    if res ==3:
        print('A')
    elif res ==2:
        print('B')
    elif res ==1:
        print('C')
    elif res ==0:
        print('D')
    elif res ==4:
        print('E')
        