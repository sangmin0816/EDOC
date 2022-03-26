import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
cards = deque([1])

for i in range(2, N+1):
    for j in range(2,i):
        cards.append(cards.popleft())
        cards.appendleft(i)

for i in cards:
    print(i)