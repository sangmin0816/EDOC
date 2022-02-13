import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))

friends = [[] for i in range(N)]

for i in range(M):
    A, B = map(int, input().split(' '))

