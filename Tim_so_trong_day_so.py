from abc import abstractproperty
from os import altsep
from typing import List


STN = [0,1,2,3,4,5,6,7,8,9]
Check = False
A = []
try:
    N = int(input('Nhập số lượng các số trong dãy: '))
    Check = True
except:
    print('Nhập sai giá trị')
if Check == True:
    print('Số lượng phần tử trong dãy là: ',N)
one = N // 10
print(one)
for i in range(N):
    A.append(i) 
    # A = print(i ,end=',')
print(A)
S = (A)
print(S)
for i in range(N):
    if S[i] % 2 == 0 and S[i] > 4:
        print(S[i],end=' ')
