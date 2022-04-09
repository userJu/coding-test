word = input()
arr = []
for i in range(len(word)):
    put = ''
    for x in word[i:]:
        put+=x
    arr.append(put)
arr.sort()
for x in arr:
    print(x)