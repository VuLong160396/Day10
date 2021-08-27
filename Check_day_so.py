ai = ai_1 = count = 0
n = int(input('Nhập n: '))
while count < n:
    ai_1 += 1
    str_ai = str(ai)
    print('a',str_ai)
    str_ai_1 = str(ai_1)
    print(str_ai_1)
    for i in(str_ai):
        for j in(str_ai_1):
            if i == j:
                break
        if i == j:
            break
    else:
        ai = ai_1
        count += 1
print('')
print(ai)
b = 456
# n = input(':: ')
# for i in range(5):
#     if n == 'a':
#         print('ok')
#         break
# else:
#     print('not n')