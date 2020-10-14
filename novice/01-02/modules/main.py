import matematika as jumlah

jumlah.tambah(6,5)
perkalian = jumlah.perkalian(9,5)
print(perkalian)

DaftarAngka = [23,7,32,99,4,15,11,20]
BubbleSort = jumlah.BubbleSort(DaftarAngka)
print(DaftarAngka)

angka = [73,2,23,43,1,21,11,50]
SelectionSort = jumlah.SelectionSort(angka)
print(angka)

nomor = [56,7,34,65,23,12,5,20]
InsertionSort = jumlah.InsertionSort(nomor)
print(nomor)

list = [67,91,87,33,49,10,16,43,65,3]
print('Data yang akan di sort :', list)
print('Quick Sort :')
qs = jumlah.qs(list,0,len(list)-1)

print('Menggabungkan List', list)
list = [2,5,60,43,27,10,89,17]
ms = jumlah.ms(list)