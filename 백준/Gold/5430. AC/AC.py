import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
	p = input().rstrip()
	n = int(input())
	I = input().rstrip()
	arr = []
	leng = ""
	for x in I:
		if x.isdecimal() == True:
			leng+=x
		else:
			if leng != "":
				arr.append(leng)
				leng = ""
	start = 0
	end = n-1
	isEmpty = False
	err = False
	if len(arr) == 0:
		isEmpty = True
        
	for x in p:
		if x == 'R':
			if isEmpty == True:
				continue
			else:
				start,end = end,start
		elif x =='D':
			if isEmpty == True or end == -1 or start == -1:
				err = True
				break
			elif start == end:
				isEmpty = True
			elif start < end:
				start+=1
			elif start > end:
				start-=1
	
	if isEmpty == False:
		if start<end:
			print(f'[{",".join(arr[start:end+1])}]')
		else:
			print(f'[{",".join(arr[end:start+1][::-1])}]')
	elif isEmpty == True:
		print('error') if err else print('[]')