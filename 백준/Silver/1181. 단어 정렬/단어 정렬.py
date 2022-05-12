import sys
input = sys.stdin.readline
N = int(input())

arr = []

for _ in range(N):
    word = input().rstrip()
    wordLen = len(word)
    arr.append((word,wordLen))
arr = set(arr)
arr = list(arr)
arr.sort(key = lambda x :(x[1],x[0]))


for x in arr:
    print(x[0])
