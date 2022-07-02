"""
기본 구현
"""
import sys
input = sys.stdin.readline
N = int(input())
dict = {}
for _ in range(N):
    word = input().split()
    dict[word[0]] = word[2]

T = int(input())
for _ in range(T):
    n = int(input())
    sent = input().split()
    for x in sent:
        print(dict[x], end=" ")
    print()

