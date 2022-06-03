n = int(input())

dy = [0,1,2]
div = 10007
if n >2:
    for i in range(len(dy),n+1):
        dy.append(dy[i-1]+dy[i-2])
    print(dy[n]%div)
else:
    print(dy[n])