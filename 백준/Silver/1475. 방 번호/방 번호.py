import sys
input = sys.stdin.readline
N = input().rstrip()
arr = [0,0,0,0,0,0,0,0,0,0]
for x in N:
    arr[int(x)]+=1
res=0
if (arr[6]+arr[9])%2 ==0:
    res+=(arr[6]+arr[9])//2
else:
    res+=(arr[6]+arr[9])//2+1
arr[6] = 0
arr[9] = 0
max_arr = max(arr)
res = max(max_arr,res)
print(res)
        

    
            
            
        
        