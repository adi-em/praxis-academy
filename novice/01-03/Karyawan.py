class Karyawan:
    '''Dasar kelas untuk semua karyawan'''
    jumlah_karyawan = 0

    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        Karyawan.jumlah_karyawan += 1

    def tampilkan_jumlah(self):
        print("Total karyawan:", Karyawan.jumlah_karyawan)

    def tampilkan_profil(self):
        print("Nama :", self.nama)
        print("Gaji :", self.gaji)
        print()

karyawan1 = Karyawan('adi', 10000)
karyawan2 = Karyawan('ida', 50000)

karyawan1.tampilkan_profil()
karyawan2.tampilkan_profil()
print("total karyawan:", Karyawan.jumlah_karyawan)
