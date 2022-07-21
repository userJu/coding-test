import sys
input = sys.stdin.buffer.readline

counts = [0 for i in range(10010)]
for n in range(int(input())):
    counts[int(input())]+=1
for i in range(10010):
    for j in range(counts[i]):
        sys.stdout.write(str(i)+"\n")

