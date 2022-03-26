import sys
input = sys.stdin.readline

while(True):
    T = input().rstrip()
    if T == '*':
        break

    Tset = set()
    flag = 0
    if len(T)==1:
        flag = 1
    else:
        for i in range(len(T)-2):
