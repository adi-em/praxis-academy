# Django

Django adalah kerangka kerja web gratis dan sumber terbuka yang ditulis dengan Python yang mengikuti pola arsitektur perangkat lunak model template view (MTV) . Pola MTV adalah Django yang mengambil pola model – view – controller (MVC) . Menurut Django Software Foundation, model adalah sumber definitif tunggal dari data Anda, view menjelaskan data yang direpresentasikan kepada pengguna melalui fungsi panggilan balik Python ke URL tertentu, dan templatnya adalah bagaimana Django menghasilkan HTML secara dinamis.

Prinsip inti Django adalah skalabilitas, kegunaan kembali dan pengembangan cepat. Ia juga dikenal karena konsistensi tingkat kerangka kerja dan kopling longgar, memungkinkan komponen individu untuk tidak bergantung satu sama lain. Jangan ulangi diri Anda sendiri ( (DRY programming ) merupakan bagian integral dari prinsip Django.

# cara instal django

Ada tiga cara untuk memasang Django. Kami akan menggunakan metode pip instalasi untuk tutorial ini, tapi mari kita bahas semua opsi yang tersedia untuk referensi Anda.

1. Pasang Django dalam a virtualenv.
Ini ideal ketika Anda membutuhkan versi Django Anda untuk diisolasi dari lingkungan global server Anda.
2. Pasang Django dari Sumber.
Jika Anda menginginkan perangkat lunak terbaru atau menginginkan sesuatu yang lebih baru dari yang ditawarkan oleh repositori Ubuntu APT Anda, Anda dapat menginstal langsung dari sumbernya. Perhatikan bahwa memilih metode penginstalan ini memerlukan perhatian dan pemeliharaan terus-menerus jika Anda ingin versi perangkat lunak Anda diperbarui.
3. Pasang Django Secara Global dengan pip.
Pilihan yang kita gunakan adalah pip 3 karena kita akan memasang Django secara global.

untuk membuat direktori bernama django-apps, atau nama lain pilihan Anda. Kemudian navigasikan ke direktori.

```mkdir django-apps```
```cd django-apps```

Saat berada di dalam django-appsdirektori, buat lingkungan virtual Anda.

```virtualenv env```

aktifkan lingkungan virtual dengan perintah

```. env/bin/activate```

unutk menginstall django dengan perintah

```pip install django```

untuk cek sudah terinstal atau belum bisa dengan perintah

```pip django-admin --version```

untuk memulai proyek bisa dengan perintah

```django-admin startproject nama project```

