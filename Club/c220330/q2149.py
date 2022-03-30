from re import L
import sys
input = sys.stdin.readline

key = list(input().rstrip())
key_sort = list()
keylen = len(key)

for i in range(keylen):
    key_sort.append([key[i], i])

key_sort.sort()

order = list()
for i in range(keylen):
    order.append(key_sort[i][1])

crypto_temp = list(input().rstrip())
cryptogram = []
column = len(crypto_temp)//keylen
for i in range(keylen):
    cryptogram.append(crypto_temp[i*column:(i+1)*column])

plain_text = ""

for j in range(column):
    temp = key
    for i in range(keylen):
        temp[order[i]] = cryptogram[i][j]
    plain_text += "".join(temp)

print(plain_text)