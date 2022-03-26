n = int(input())
i=0
beehouse=1
while n > beehouse : # 벌집의 위치를 찾을때까지
    i+=1
    beehouse+=6*i
print(i+1)
    