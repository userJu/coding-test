arr = []
for i in range(9):
    arr.append(int(input()))
sums = sum(arr)

def F():
    for i in range(8):
        for j in range(i+1,9):
            if sums - (arr[i]+arr[j]) == 100:
                return [arr[i],arr[j]]


res = set(arr)-set(F())
res = sorted(list(res))
for x in res:
    print(x)

