import sys
a,b = map(str, sys.stdin.readline().split())
# '734', '893'
x = a[::-1]
y = b[::-1]
ax=''
by=''
for i in range(3):
    ax+=x[i]
    by+=y[i]
print(max(int(ax),int(by)))