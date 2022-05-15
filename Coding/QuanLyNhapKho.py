print('A: Nhập hàng hóa.')
print('B: Kiểm kê hàng hóa.')
print('C: Thoát.')
chon_chuc_nang='y'
a='STT'
b='Tên hàng hóa'
c='Số lượng'
d='Ngày nhập'
e='Nhà cung cấp'
while chon_chuc_nang!='c' or chon_chuc_nang!='C':
	chon_chuc_nang = str(input('Chọn chức năng: '))

	#Thoát
	if chon_chuc_nang=='c' or chon_chuc_nang=='C':
		break

	#Add hàng tồn kho
	elif chon_chuc_nang=='A' or chon_chuc_nang=='a':
		ngay_nhap={}
		ten_hang={}
		so_luong={}
		nha_cung_cap={}
		stt=int(input('Số thứ tự: '))
		th=str(input('Tên hàng hóa: '))
		sl=int(input('Số lượng: '))
		ncc=str(input('Nhà cung cấp: '))
		ngnh=str(input('Ngày nhập: '))
		QLHTK=open('HangTonKho.txt','w')
		QLHTK.write(str(stt))
		QLHTK.write(str(th))
		QLHTK.write(str(sl))
		QLHTK.write(str(ncc))
		QLHTK.write(str(ngnh))
		QLHTK=open('HangTonKho.txt','r')
		ten_hang.update({stt:th})
		so_luong.update({stt:sl})
		nha_cung_cap.update({stt:ncc})
		ngay_nhap.update({stt:ngnh})
		print(a.ljust(17, ' '), end='')
		print(b.ljust(27, ' '), end='')
		print(c.ljust(21, ' '), end='')
		print(d.ljust(21, ' '), end='')
		print(e.rjust(20, ' '))
		print(str(stt).ljust(20,' '),end='')
		print(ten_hang.get(stt).ljust(27, " "), end='')
		print(str(so_luong.get(stt)).ljust(18, ' '), end='')
		print(ngay_nhap.get(stt).ljust(31, ' '), end=' ')
		print(nha_cung_cap.get(stt))



