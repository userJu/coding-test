n = int(input())
factorial = 1
cnt=0
for i in range(1,n+1):
    factorial=factorial * i
factorial = str(factorial)
for x in factorial[::-1]:
    if int(x) == 0:
        cnt+=1
    else:
        break
print(cnt)