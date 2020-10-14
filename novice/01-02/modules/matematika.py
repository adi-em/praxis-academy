def tambah (a,b):
    print('penambahan')
    print(a,'+',b,'=',a+b)

def perkalian(a,b):
    print('perkalian')
    return a * b

def BubbleSort(val):
    for namber in range(len(val)-1,0,-1):
        for i in range(namber):
            if val[i]>val[i+1]:
                temp = val[i]
                val[i] = val[i+1]
                val[i+1] = temp

def SelectionSort(val):
   for isi in range(len(val)-1,0,-1):
       Max=0
       for lokasi in range(1,isi+1):
           if val[lokasi]>val[Max]:
               Max = lokasi
 
       temp = val[isi]
       val[isi] = val[Max]
       val[Max] = temp

def InsertionSort(val):
   for index in range(1,len(val)):

     valueaktif = val[index]
     posisi = index

     while posisi>0 and val[posisi-1]>valueaktif:
         val[posisi]=val[posisi-1]
         posisi = posisi-1

     val[posisi]=valueaktif

def qs(list,awal,akhir):
    if awal < akhir:
        pindex = partisi(list,awal,akhir)
        qs(list,awal,pindex-1)
        qs(list,pindex+1,akhir)
def partisi(list,awal,akhir):
    tengah = int(akhir/2)
    pivot = list[tengah]
    pindex = awal
    for i in range(awal,tengah):
        if list[i]>=pivot:
            list[i],list[pindex]=list[pindex],list[i]
            pindex = pindex + 1
    list[pindex],list[tengah]=list[tengah],list[pindex]
    print(list)
    return pindex


def ms(list):
    print('Memecah List', list)
    n = len(list)
    if n < 2:
        return list
    else:
        mid=n//2
        left=list[:mid]
        right=list[mid:]
        ms(left)
        ms(right)
        i=0
        j=0
        k=0
        while i < len (left) and j < len (right):
            if left[i]>right[j]:
                list[k]=left[i]
                i=i+1
            else:
                list[k]=right[j]
                j=j+1
            k=k+1
        while i < len (left):
            list[k]=left[i]
            i=i+1
            k=k+1
        while j < len (right):
            list[k]=right[j]
            j=j+1
            k=k+1
    


 


