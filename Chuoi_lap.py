Enter = input('Nhập chuỗi: ')
Size = len(Enter)
Center = Size//2
Emer = False
if Size % 2 != 0:
    if Enter.count(Enter[0]) == Size:
        print('Chuỗi cần check: ',Enter[0])
        print(f'Lặp {Size} lần')
        print('Đây là chuỗi lặp!!!')
    else:
         print('Đây không phải chuỗi lặp!!!')
else:
    if Enter[None:Center] == Enter[Center:None]:
        print('Chuỗi cần check: ',Enter[None:Center])
        print('Lặp 2 lần')
        print('Đây là chuỗi lặp!!!')
        #kiểm tra số lần xuất hiện của  ký tự chạy từ 1 đến Center
#print(Enter.count('a'))#in ra số lần xuất hiện của ký tự 'a'
    else:
        for i in range (1,Center,1):
            Check = (Enter[None:i]) #chuỗi nhỏ chạy từ 1 ký tự đến gần nửa chuỗi lớn
            Size_Check = len(Check) #Độ dài của chuỗi nhỏ
            repeat = Enter.count(Check) #Số lần xuất hiện của chuỗi nhỏ
            Present = int(Size / Size_Check) #Số lần có mặt để đủ chuỗi lớn
            if repeat == Present:
                print('Chuỗi cần check: ',Check)
                print(f'Lặp {repeat} lần')
                print('Đây là chuỗi lặp!!!')
            elif Size_Check == Center - 1:
                print('Đây không phải là chuỗi!!!')
                break
