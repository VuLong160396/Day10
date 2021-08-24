Request = 0
while Request != 0 or Request != 1:
    Request = int(input('Yêu cầu mã hóa chọn (0) hoặc giải mã chọn (1): '))
    if Request == 1 or Request == 0:
        break
#Nhập chuỗi:
for i in range(True):
    Enter = input('Mời nhập chuỗi: ')
    if len(Enter) > 0:
        break
size = int(input('Mời nhập số ký tự ban đầu: '))
#Xử lý mã hóa
def coding():
    Sb = Enter[None:size]
    Se = Enter[size:None]
    Sb_code = Sb[::-1] #Đảo ngược ký tự chuỗi
    Se_code = Se[::-1] #Đảo ngược ký tự chuỗi
    S = Sb_code + Se_code
    print('Chuỗi sau khi mã hóa là:',S)
#Xử lý giải mã
def encoding():
    Sb = Enter[None:size]
    Se = Enter[size:None]
    Sb_code = Sb[::-1] #Đảo ngược ký tự chuỗi
    Se_code = Se[::-1] #Đảo ngược ký tự chuỗi
    Q = Sb_code + Se_code
    print('Chuỗi sau khi mã hóa là:',Q)
if Request == 0:
    coding()
else:
    encoding()
