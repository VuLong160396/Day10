condition = False
byte = 4096
try:
    Size_of_file = int(input('Nhập dung lượng file(byte): '))
    condition = True
    if condition == True and Size_of_file > 0:
        big = Size_of_file // byte
        small = Size_of_file % byte
        if big <= 0 and small > 0:
            print('File có dung lượng 1KB')
        elif big > 0 and small == 0:
            print('File có dung lượng', big ,'KB')
        elif big > 0 and small > 0:
            print('File có dung lượng ', big + 1,'KB')
except:
    print('Value is invalid')