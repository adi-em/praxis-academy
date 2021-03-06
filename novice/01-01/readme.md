# minggu 1

## hari ke-1 python, mengenal bahasa pemrograman
 
### 1. bahasa pemrograman https://id.wikipedia.org/wiki/Bahasa_pemrograman
  
   macam-macam bahasa pemrograman:
   - Bahasa pemrograman C  (kategori tingkat tinggi) https://id.wikipedia.org/wiki/C_(bahasa_pemrograman)
   - Bahasa pemograman JAVA (kategori tingkat tinggi) https://id.wikipedia.org/wiki/Java
   - Bahasa pemograman PYTHON https://id.wikipedia.org/wiki/Python_(bahasa_pemrograman)
   - Bahasa pemograman RUBY https://id.wikipedia.org/wiki/Ruby_(bahasa_pemrograman)
   - Bahasa pemograman PHP https://id.wikipedia.org/wiki/PHP
   - Bahasa pemograman MICROSOFT VISUAL BASIC https://id.wikipedia.org/wiki/Visual_Basic
   - Bahasa pemograman VISUAL C++ https://id.wikipedia.org/wiki/Visual_C%2B%2B
   - Bahasa pemograman DELPHI https://id.wikipedia.org/wiki/Embarcadero_Delphi
   - ahasa pemograman C++ https://id.wikipedia.org/wiki/C%2B%2B
   - Bahasa Pemrograman Javascript https://id.wikipedia.org/wiki/JavaScript

### 2. sejarah dan pengertian python


Python diciptakan oleh Guido van Rossum pertama kali di  Centrum Wiskunde & Informatica (CWI) di Belanda pada awal tahun 1990-an. Bahasa python terinspirasi dari bahasa pemrograman ABC. Sampai sekarang, Guido masih menjadi penulis utama untuk python, meskipun bersifat open source sehingga ribuan orang juga berkontribusi dalam mengembangkannya.

Di tahun 1995, Guido melanjutkan pembuatan python di Corporation for National Research Initiative (CNRI) di Virginia Amerika, di mana dia merilis beberapa versi dari python.

Pada Mei 2000, Guido dan tim Python pindah ke BeOpen.com dan membentuk tim BeOpen PythonLabs. Di bulan Oktober pada tahun yang sama, tim python pindah ke Digital Creation (sekarang menjadi Perusahaan Zope). Pada tahun 2001, dibentuklah Organisasi Python yaitu Python Software Foundation (PSF). PSF merupakan organisasi nirlaba yang dibuat khusus untuk semua hal yang berkaitan dengan hak intelektual Python. Perusahaan Zope menjadi anggota sponsor dari PSF.

Semua versi python yang dirilis bersifat open source. Dalam sejarahnya, hampir semua rilis python menggunakan lisensi GFL-compatible. 

Berikut adalah versi mayor dan minor python berikut tanggal rilisnya.
    
- Python 1.0 – Januari 1994
- Python 1.2 – 10 April 1995
- Python 1.3 – 12 Oktober 1995
- Python 1.4 – 25 Oktober 1996
- Python 1.5 – 31 Desember 1997
- Python 1.6 – 5 September 2000
- Python 2.0 – 16 Oktober 2000
- Python 2.1 – 17 April 2001
- Python 2.2 – 21 Desember 2001
- Python 2.3 – 29 Juli 2003
- Python 2.4 – 30 Nopember 2004
- Python 2.5 – 19 September 2006
- Python 2.6 – 1 Oktober 2008
- Python 2.7 – 3 Juli 2010
- Python 3.0 – 3 Desember 2008
- Python 3.1 – 27 Juni 2009
- Python 3.2 – 20 Februari 2011
- Python 3.3 – 29 September 2012
- Python 3.4 – 16 Maret 2014
- Python 3.5 – 13 September 2015
- Python 3.6 – 23 Desember 2016
- Python 3.7 – 27 Juni 2018

Nama python sendiri tidak berasal dari nama ular yang kita kenal. Guido adalah penggemar grup komedi Inggris bernama Monty Python. Ia kemudian menamai bahasa ciptaannya dengan nama Python.

### 3. pengertian pip

PIP merupakan Package Management System yang digunakan untuk mengunduh dan mengelola package Python. ada ribuan package yang bisa kita temukan di PyPI. semacam apt-get kalau kita main di linux.

untuk menginstall pip pada linux dengan perintah

`sudo apt-get install python3-pip`

untuk mengunduh dan menginstal package yang terbaru

`pip3 install <nama-package>`

untuk menampilkan package-package yang sudah diinstal gunakan perintah

`pip3 list`

menguninstall package di PIP

`pip3 uninstall <nama-package>`

untuk menguninstall banyak paket dalam satu kali uninstall

`pip3 uninstall -r requirements.txt`


### 4. pengertian jupyter

jupyter adalah organisasi non-profit untuk mengembangkan software interaktif dalam berbagai bahasa pemrograman. Notebook adalah satu software buatan Jupyter, adalah aplikasi web open-source yang memungkinkan Anda membuat dan berbagi dokumen interaktif yang berisi kode live, persamaan, visualisasi, dan teks naratif yang kaya.

Mungkin penjelasan di atas kurang jelas. Ilustrasinya begini. Dulu, biasanya kita membagikan kode dan dokumen secara terpisah. Kode-kode kita satukan dalam sebuah librari/aplikasi/proyek (Visual Studio, Eclipse, dsb), dan dokumen kita buat dengan penyunting kata. Dalam dokumen bisa tampilkan cuplikan kode, tampilan hasil, dan visualisasi lainnya dari program kita.

Nah Jupyter Notebook menyatukan semua ini, baik itu teks/narasi, kode hidup, persamaan, tampilan hasil, gambar statis, dan visualisasi grafis, dalam satu file interaktif. Dan, kelebihan lainnya, notebook dapat dijalankan ulang oleh siapapun yang membukanya, untuk mereproduksi eksekusi kode di dalamnya.

Contohnya adalah dokumen ini sendiri. Dokumen ini aslinya adalah sebuah Jupyter Notebook. Mungkin Anda membacanya di blog IndoML, karena notebook ini telah dikonversi menjadi blog WordPress dengan menggunakan utilitas nb2wp. Anda bisa melihat file aslinya di GitHub, dan akan tampak keluaran yang sama.

cara install jupyter 

`pip3 install jupyterlab`

atau bisa menggunakan perintah 

`python3 -m pip install jupyterlab`

untuk membuka jupyterlab bisa dengan perintah 

`jupyter lab`

### 5. Pengertian Compiler

Compiler adalah suatu program yang menerjemahkan bahasa program ( source code) kedalam bahasa objek (obyek code). Compiler menggabungkan keseluruhan bahasa program, mengumpulkannya dan kemudian menyusunnya kembali.

Komplier memerlukan waktu untuk membuat suatu program dapat di eksekusi oleh computer, program yang dieksekusi oleh compiler adalah dapat berjalan lebih cepat disbanding program yang diperoduksi oleh interpreter, disamping itu juga bersifat independen. Contoh program yang menggunakan compiler adalah Visual Basic, Visual Delvi, dan Pascal.

Tahap Kompilasi:
- Pertama source code (program yang ditulis) dibaca kememori computer).
- Source code tersebut diubah menjadi objek code (bahasa Assembly).
- Objek code di hubungkan dengan liberary yang dibutuhkan untuk membentuk file yang bisa dieksekusi.

### 6. Pengertian Interpreter

Interpreter adalah Perangkat lunak yang mampu mengeksekusi code program (yang ditulis oleh programmer) lalu menterjemahkannya ke dalam bahasa mesin, sehingga mesin melakukan instruksi yang diminta oleh programmer tersebut. Perintah-perintah yang dibuat oleh programmer tersebut dieksekusi baris demi baris, sambil mengikuti logika yang terdapat di dalam kode tersebut.

Proses ini sangat berbeda dengan compiler, dimana pada compiler, hasilnya sudah langsung berupa satu kesatuan perintah dalam bentuk bahasa mesin, dimana proses penterjemahan dilaksanakan sebelum program tersebut dieksekusi.

Interpreter atau dalam bahasa Indonesia dikenal sebagai Juru Bahasa berbeda dengan Translator atau penterjemah dalam segi media yang dipakai untuk menerjemahkan. Interpreter akan menterjemahkan bahasa sumber ke dalam bahasa sasaran secara langsung atau orally sementara translator akan menerjemahkan bahasa sumber ke bahasa sasaran secara tertulis.

Java dijalankan menggunakan interpreter yaitu Java Virtual Machine (JVM). Hal ini menyebabkan source code Java yang telah dikompilasi menjadi Java bytecodes dapat dijalankan pada platform yang berbeda-beda.

sumber https://www.pythonindo.com/sejarah-python/

terimakasih sudah untuk membaca 
