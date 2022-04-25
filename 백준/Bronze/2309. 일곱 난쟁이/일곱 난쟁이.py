import sys

input = sys.stdin.readline
arr=[]

for _ in range(9):
    arr.append(int(input()))
sums = sum(arr)
one = 0
two = 0  
for j in range(8):
    for k in range(j+1,9):
        if sums-(arr[k]+arr[j]) == 100:
            one,two = arr[j], arr[k]
            break

arr.remove(one)
arr.remove(two)
arr.sort()
for x in arr:
    print(x)