# 정확히 N 배달
# 봉지는 3과 5
# 더 적은 개수의 봉지 가져가기
N = int(input())
cnt=0
while N >=0:
    if N % 5 == 0:
        cnt+=int(N//5)
        print(cnt)
        break
    N-=3
    cnt+=1
    
else:
    print(-1)
            