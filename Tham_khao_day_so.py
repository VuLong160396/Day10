n = int(input("Nhập n:"))
f=0 #biến dùng để gán ai cho ai_1 1 lần duy nhất
ai=0 #giá trị ai
ai_1=0 #giá trị a(i-1)
for h in range (0,n):
    #Vòng lặp cộng cho đến khi ai không trùng số với ai_1
    while True:
        e=0 #tham số để so sánh cộng hay thoát lặp
        if f==0:
            ai_1=ai
        chuoi_ai=str(ai)
        chuoi_ai_1=str(ai_1)
        #kiểm tra ai có nằm trong ai_1 không
        for i in range (0,len(chuoi_ai)):
            for d in range (0,len(chuoi_ai_1)):
                if chuoi_ai[i]==chuoi_ai_1[d]:
                    e=e+1
        if e!=0:
            f=1
            ai=ai+1
        else:
            break
    f=0
print(ai)
