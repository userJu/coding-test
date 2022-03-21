import sys
s = sys.stdin.readline().strip()
for i in range(97,123):
    idx = s.find(chr(i))
    print(idx, end=" ")
