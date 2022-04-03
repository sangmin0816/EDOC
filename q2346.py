from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
balloons = list(map(int, input().split(' ')))
b_deq = deque()

for b in range(len(balloons)):
    b_deq.append([b, balloons[b]])

ans = []

index = 0

while(len(b_deq)):
    if index>=0:
        while(index!=0):
            b_deq.append(b_deq.popleft())
            index -= 1
        index = b_deq[0][1]-1
        ans.append(b_deq.popleft())
    else:
        while(index!=0):
            b_deq.append(b_deq.popleft())
            index += 1
        index = b_deq[0][1]+1
        ans.append(b_deq.pop())

for a in ans:
    print(a[0]+1, end=' ')