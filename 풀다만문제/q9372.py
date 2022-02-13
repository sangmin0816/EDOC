from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N, M = map(int, input().split(' '))
    airplanes = [[] for l in range(N+1)]

    for j in range(M):
        a, b = map(int, input().split(' '))
        airplanes[a].append(b)
        airplanes[b].append(a)