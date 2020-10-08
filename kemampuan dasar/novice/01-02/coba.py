a = ["apple", "banana", "cherry"]

b = ["Ford", "BMW", "Volvo"]

a.append(b)

print(a)

#menambahkan di belakang

fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

print(fruits)
#menggabungkan fruits dan cars

fruits = ['apple', 'banana', 'cherry']

fruits.pop(1)

print(fruits)
#menampilkan isi dari pertama

fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")

print(fruits)
#menambahkan 1 buah ke posisi no 1

fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

print(x)
#mencari posisi no opjek

fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana")

print(fruits)
#menghapus dengan nama objek

fruits = ["apple", "banana", "cherry"]

fruits.clear()

print(fruits)
#menghapus semua isi di array