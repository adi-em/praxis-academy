import pickle

#Berikut adalah contoh dict
name = { 'adi': 100, 'rob': 72, 'susi': 87 }

#Gunakan dump untuk mengubah objek menjadi string serial
serial_name = pickle.dumps( name )
print(serial_name)
#Gunakan loads untuk membatalkan serialisasi objek
received_name = pickle.loads( serial_name )
print(received_name)