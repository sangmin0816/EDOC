from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))

tiles = list()

for i in range(N):
    tiles.append(list(input().strip()))

ans = 0
visited = [[0]*M]*N

for i in range(N):
    for j in range(M):
        if(visited[i][j]==0):
            ans+=1
            if(tiles[i][j]=='|'):
                for k in range(j, M):
                    if(tiles[i][k]!='|'):
                        break
                    visited[i][k]=1
            elif(tiles[i][j]=='-'):
                for k in range(i, N):
                    if(tiles[k][j]!='-'): 
                        break
                    visited[k][j]=1

print(ans)