a,b,v = map(int, input().split())
# day의 값만큼 while을 돌아야 하는 문제가 있다
day = (v-b)/(a-b)
print(int(day) if day == int(day) else int(day)+1)	#삼항연산자
    
    