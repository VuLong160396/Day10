m = 1234
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
# one = N // 10
# print(one)
for i in range(N):
    A.append(i) 
print(A)
S = (A)
B = (str(S[-1])).split()
# print(B)
for i in str(B):
    print(i,end= ' ')

# for i in range(N):
#     if S[i] % 2 == 0 and S[i] > 4:
#         print(S[i],end=' ')
