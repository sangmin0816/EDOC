from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    N, M = map(int, input().split(' '))
    arr = deque(list(map(int, input().split(' '))))