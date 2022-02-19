import sys
input = sys.stdin.readline

N = int(input())

dparr = [0 for i in range(N+1)]

def dp(index):
    if(index==1):
        return
    elif(index==2):
        dparr[index]=2
        return
    elif(dparr[index]==0):
        if(index%2==0):
            dp(index//2)
            dparr[index] = 2*dparr[index//2] + index
        else:
            dp(index-1)
            dparr[index] = dparr[index-1] + 1
        return

dp(N)
ans = dparr[N]
print(dparr)
print(ans)