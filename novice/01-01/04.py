def InsertionSort(val):
   for index in range(1,len(val)):

     valueaktif = val[index]
     posisi = index

     while posisi>0 and val[posisi-1]>valueaktif:
         val[posisi]=val[posisi-1]
         posisi = posisi-1

     val[posisi]=valueaktif

DaftarAngka = [56,7,34,65,23,12,5,20]
InsertionSort(DaftarAngka)
print(DaftarAngka)