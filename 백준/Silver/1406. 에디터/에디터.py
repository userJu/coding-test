import sys
from collections import deque
input = sys.stdin.readline
word = input().rstrip()
left = deque([])
right = deque([])
for x in word:
    left.append(x)
for _ in range(int(input())):
    cmd = input().rstrip()
    if cmd[0] == 'L':
        if left:
            right.appendleft(left.pop())
    elif cmd[0] == 'D':
        if right:
            left.append(right.popleft())
    elif cmd[0] == 'B':
        if left:
            left.pop()
    elif cmd[0] == 'P':
        left.append(cmd[2])
left.extend(right)
print("".join(left))
        
        