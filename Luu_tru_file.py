condition = False
byte = 4096
try:
    Size_of_file = int(input('Nhập dung lượng file(byte): '))
    condition = True
    if condition == True and Size_of_file > 0:
        big = Size_of_file // byte
        small = Size_of_file % byte
        if big <= 0 and small > 0:
            print('File có dung lượng 4KB')
        elif big > 0 and small == 0:
            print('File có dung lượng', big*4 ,'KB')
        elif big > 0 and small > 0:
            print('File có dung lượng ', (big + 1)*4,'KB')
except:
    print('Value is invalid')

#Cách 2
if Size_of_file <= 4096:
    print('Dung lượng file 4KB')
box = Size_of_file % byte
if  box == 0:
    print('Dung lượng file: ',box * 4 ,'KB')
else:
    print('Dung lượng file:',(box + 1) * 4,'KB')