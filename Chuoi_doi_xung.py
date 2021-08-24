Enter = input('Mời nhập chuỗi: ')
Size = len(Enter)
print('Độ dài của chuỗi:',Size,'ký tự')
origin = Size // 2
add = Size % 2
if add > 0:
    # print(Enter[origin])
    before = Enter[None:origin] #Vị trí nửa đầu trái phần tử (None) đến phần tử trung tâm
    after = Enter[origin+1:None]#Vị trí nửa sau phần tử trung tâm đến phần tử cuối cùng (None)
    # print(before)
    # print(after)
    if before == after[::-1]:#Đảo ký tự của chuỗi after
        print('Đây là chuỗi đối xứng')
    else:
        print('Đây không phải chuỗi đối xứng!!!!')
else:
    before = Enter[None:origin]
    after = Enter[origin:None]
    # print(before)
    # print(after)
    if before == after[::-1]: 
        print('Đây là chuỗi đối xứng')
    else:
        print('Đây không phải chuỗi đối xứng!!!!')