#2차원 배열 만드는 법 까먹었다 ㅋㅋㅋ
# 으엥 어려워

n = int(input())
coo = []
for i in range(n):
    coo.append(list(map(int, input().split(' '))))

ans = 0

coo.sort(key=lambda x:x[0])
stdx = coo[0][0]
stdy = coo[0][1]
for i in range(n-1):
    if(stdx == coo[i+1][0]):
        if(stdy!=coo[i+1][1]): ans+=1
    else:
        stdx = coo[i+1][0]
        stdy = coo[i+1][1]

coo.sort(key=lambda x:x[1])
stdy = coo[0][1]
for i in range(n-1):
    if(stdy == coo[i+1][1]): ans+=1
    else:
        stdy = coo[i+1][1]

print(ans)