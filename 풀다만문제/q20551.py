# 시간 초과가 자꾸 난다. 어렵구만

import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))

arrA = [int(input()) for i in range(N)]
arrA.sort()

def binarySearch(arr, key):
    left = 0
    right = len(arr)-1
    
    while right >= left:
        mid = (left+right)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            right = mid - 1
        elif arr[mid] < key:
            left = mid + 1
    
    return -1

for i in range(M):
    q = int(input())
    a = binarySearch(arrA, q)
    if a != -1 :
        for j in range(a, -1, -1):
            if arrA[a] == arrA[j]:
                a = j
            else:
                break
    print(a)