data = open('/Users/thinhpld0/Desktop/code/funix_ex/diemtrungbinh.txt')
dic=[]
dic_id_xeploai={}
lis=[]
tunhien=[]
xahoi=[]
dic_xeploai_khoi={}
dic_main={}
for conten in data:                    # gán dữ liệu
    conten = conten.rstrip()           #xoá khoảng trắng
    if conten.startswith('Ma'):        #nếu dòng bđâu 'Ma' thì bỏ
        continue
    words = conten.split()
    dic.extend([words])                #gắn từng người theo lần lượt [1,2,3,4,5,6]

def xeploai_hocsinh(id) :              #xếp loại từng hs
    x = id-1
    a = dic[x]                           #in dòng 
    b = a[2]                            #lấy phần tử thứ 2 ( điểm )
     # điểm môn 1         EX: output: str: 7.6,5.85;6.95;6.65;8.1;6.75;8.1;7.05
    d= b.replace(';',' ')    #bỏ phần ';' thay bằng ' '
    c = d.split()
    diem_toan =float(c[0])
    diem_ly = float(c[1])
    diem_hoa = float(c[2])
    diem_sinh =float(c[3])
    diem_van =float(c[4])
    diem_anh = float(c[5])
    diem_su= float(c[6])
    diem_dia = float(c[7])
    dtb_chuan = round(   ( ((diem_toan + diem_van + diem_anh) * 2 + (diem_ly + diem_hoa + diem_sinh + diem_su + diem_dia) * 1) / 11 )   ,2)
    if dtb_chuan>=9.0 and diem_toan >=8.0 and diem_ly >=8.0 and diem_hoa >8.0 and diem_sinh>=8.0 and diem_van>=8.0 and diem_anh >=8.0 and diem_su >=8.0 and diem_dia>8.0:
        dic_id_xeploai[f'Mã số {id}'] = "XUẤT SẮC"
        return 'XUAT SAC'
    elif dtb_chuan>=8.0 and diem_toan >=6.5 and diem_ly >=6.5 and diem_hoa >=6.5 and diem_sinh >= 6.5 and diem_van>=6.5 and diem_anh >=6.5 and diem_su >=6.5 and diem_dia>=6.5:
        dic_id_xeploai[f'Mã số {id}'] = "GIỎI"
        return 'GIOI'
    elif dtb_chuan>=6.5 and diem_toan >=5.0 and diem_ly >=5.0 and diem_hoa >=5.0 and diem_sinh >= 5.0 and diem_van>=5.0 and diem_anh >=5.0 and diem_su >=5.0 and diem_dia>=5.0:
        dic_id_xeploai[f'Mã số {id}'] = "KHÁ"
        return "KHA"
    elif dtb_chuan>=6.0 and diem_toan >=4.5 and diem_ly >=4.5 and diem_hoa >=4.5 and diem_sinh >= 4.5 and diem_van>=4.5 and diem_anh >=4.5 and diem_su >=4.5 and diem_dia>=4.5:
        dic_id_xeploai[f'Mã số {id}'] = "TB KHÁ"
        return 'TB KHA'
    else:
        dic_id_xeploai[f'Mã số {id}'] = "TRUNG BÌNH"
        return 'TRUNG BINH'
def output_xeploai():                          # in 
    for i in range (1,7):              #chạy vòng lặp tất cả các mã hs được lưu vào dic_id
        xeploai_hocsinh(i)             #chạy hàm trên để nhận giá trị 
        dic_id_xeploai[f'Mã số {i}']           #Đọc key , value 
    print(dic_id_xeploai)
def Khoi_A0(id) :             #xếp loại từng hs
    x = id-1
    a = dic[x]                           #in dòng 
    b = a[2]                            #lấy phần tử thứ 2 ( điểm )
     # điểm môn 1         EX: output: str: 7.6,5.85;6.95;6.65;8.1;6.75;8.1;7.05
    d= b.replace(';',' ')    #bỏ phần ';' thay bằng ' '
    c = d.split()
    diem_toan =float(c[0])
    diem_ly = float(c[1])
    diem_hoa = float(c[2])
    diem_sinh =float(c[3])
    diem_anh = float(c[5]) 

    khoi_A00 =diem_toan+diem_ly+diem_hoa
    khoi_A01 =diem_toan+diem_ly+diem_anh
    khoi_B = diem_toan+diem_sinh+diem_hoa
    tu_nhien= [khoi_A00,khoi_A01,khoi_B]

    if tu_nhien[0] >= 24:
        return('1')
    elif 18 <= tu_nhien[0] < 24:
        return('2')
    elif 12 <= tu_nhien[0] < 18:
        return('3')
    else:
        return('4')
def Khoi_A1(id) :             #xếp loại từng hs
    x = id-1
    a = dic[x]                           #in dòng 
    b = a[2]                            #lấy phần tử thứ 2 ( điểm )
     # điểm môn 1         EX: output: str: 7.6,5.85;6.95;6.65;8.1;6.75;8.1;7.05
    d= b.replace(';',' ')    #bỏ phần ';' thay bằng ' '
    c = d.split()
    diem_toan =float(c[0])
    diem_ly = float(c[1])
    diem_hoa = float(c[2])
    diem_sinh =float(c[3])
    diem_anh = float(c[5]) 
    
    khoi_A00 =diem_toan+diem_ly+diem_hoa
    khoi_A01 =diem_toan+diem_ly+diem_anh
    khoi_B = diem_toan+diem_sinh+diem_hoa

    tu_nhien= [khoi_A00,khoi_A01,khoi_B]

    if tu_nhien[1] >= 24:
        return('1')
    elif 18 <= tu_nhien[1] < 24:
        return('2')
    elif 12 <= tu_nhien[1] < 18:
        return('3')
    else:
        return('4')
def Khoi_B(id) :              #xếp loại từng hs
    x = id-1
    a = dic[x]                           #in dòng 
    b = a[2]                            #lấy phần tử thứ 2 ( điểm )
     # điểm môn 1         EX: output: str: 7.6,5.85;6.95;6.65;8.1;6.75;8.1;7.05
    d= b.replace(';',' ')    #bỏ phần ';' thay bằng ' '
    c = d.split()
    diem_toan =float(c[0])
    diem_ly = float(c[1])
    diem_hoa = float(c[2])
    diem_sinh =float(c[3])
    diem_anh = float(c[5]) 

    khoi_A00 =diem_toan+diem_ly+diem_hoa
    khoi_A01 =diem_toan+diem_ly+diem_anh
    khoi_B = diem_toan+diem_sinh+diem_hoa

    tu_nhien= [khoi_A00,khoi_A01,khoi_B]

    if tu_nhien[2] >= 24:
        return('1')
    elif 18 <= tu_nhien[2] < 24:
        return('2')
    elif 12 <= tu_nhien[2] < 18:
        return('3')
    else:
        return('4')
def Khoi_C(id) :              #xếp loại từng hs
    x = id-1
    a = dic[x]                           #in dòng 
    b = a[2]                            #lấy phần tử thứ 2 ( điểm )
     # điểm môn 1         EX: output: str: 7.6,5.85;6.95;6.65;8.1;6.75;8.1;7.05
    d= b.replace(';',' ')    #bỏ phần ';' thay bằng ' '
    c = d.split()
    diem_toan =float(c[0])
    diem_van =float(c[4])
    diem_anh = float(c[5]) 
    diem_su= float(c[6])
    diem_dia = float(c[7])

    khoi_C = diem_van +diem_su+diem_dia
    khoi_D = diem_van +diem_toan+diem_anh*2

    xa_hoi = [khoi_C,khoi_D]

    if xa_hoi[0] >= 21:
        return('1')
    elif 15 <= xa_hoi[0] < 21:
        return('2')
    elif 12 <= xa_hoi[0] < 15:
        return('3')
    else:
        return('4')
def Khoi_D(id) :              #xếp loại từng hs
    x = id-1
    a = dic[x]                           #in dòng 
    b = a[2]                            #lấy phần tử thứ 2 ( điểm )
     # điểm môn 1         EX: output: str: 7.6,5.85;6.95;6.65;8.1;6.75;8.1;7.05
    d= b.replace(';',' ')    #bỏ phần ';' thay bằng ' '
    c = d.split()
    diem_toan =float(c[0])
    diem_van =float(c[4])
    diem_anh = float(c[5]) 
    diem_su= float(c[6])
    diem_dia = float(c[7])

    khoi_C = diem_van +diem_su+diem_dia
    khoi_D = diem_van +diem_toan+diem_anh*2

    xa_hoi = [khoi_C,khoi_D]

    if xa_hoi[1] >= 21:
        return('1')
    elif 15 <= xa_hoi[1] < 21:
        return('2')
    elif 12 <= xa_hoi[1] < 15:
        return('3')
    else:
        return('4')
    
for id in range(1,7):             #gán giá trị vào: dic_xeploai
    x = id -1
    dic_xeploai_khoi[f'Mã số {id}'] = [Khoi_A0(id),Khoi_A1(id),Khoi_B(id),Khoi_C(id),Khoi_D(id)]

def main():
    for id in range(1,7):             #gán giá trị vào: dic_xeploai
        x = id -1
        dic_xeploai_khoi[f'Mã số {id}'] = [Khoi_A0(id),Khoi_A1(id),Khoi_B(id),Khoi_C(id),Khoi_D(id)]

    file_object = open('/Users/thinhpld0/Desktop/code/funix_ex/danhgia_hocsinh.txt.txt', mode= 'w')

    file_object.write('Ma HS; xeploai_TB chuan; xeploai_A; xeploai_A1; xeploai_B; xeploai_C; xeploai_D \n' )
    for id in range(1,7):      #chạy vòng lặp nhập từng tên hs và điểm vào file txt
        file_object.write(f'{id} ;{xeploai_hocsinh(id)};{Khoi_A0(id)};{Khoi_A1(id)};{Khoi_B(id)};{Khoi_C(id)};{Khoi_D(id)} \n')
        continue
    file_object.close()



print(' Câu A: Xếp loại từng học sinh ')
output_xeploai()

print()
print(' Câu B: Xếp loại điểm thi từng khối của học sinh ')
print(dic_xeploai_khoi)

print()
print(' Câu C:  Lưu bảng điểm ra 1 file “danhgia_hocsinh.txt” ')
main()
