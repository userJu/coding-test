import sys
n = int(input())
narr = sorted(list(map(int, sys.stdin.readline().split())))
m = int(input())
marr = list(map(int, sys.stdin.readline().split()))

def find(x):
    lt = 0
    rt = n-1
    while lt <=rt:
        mid = (lt + rt)//2
        if narr[mid] == x:
            return True
        if x < narr[mid]:
            rt = mid-1
        elif x > narr[mid]:
            lt = mid+1

for x in marr:
    if find(x) :
        print(1)
    else:
        print(0)

    