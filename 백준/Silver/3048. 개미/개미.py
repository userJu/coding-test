import sys
input = sys.stdin.readline
N1,N2 = map(int,input().split())
arr1 = list(input().rstrip())
arr2 = list(input().rstrip())
arr1 = arr1[::-1]
arr = arr1+arr2
T = int(input())

for _ in range(T):
    for i in range(len(arr)-1):
        if arr[i] in arr1 and arr[i+1] in arr2:
            arr[i],arr[i+1] = arr[i+1],arr[i]
            if arr[i+1] == arr1[-1]:
                break
print("".join(arr))
    
        