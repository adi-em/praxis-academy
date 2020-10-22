# instal postgresql

sebelum instal postgresql update terlebih dahulu

```sudo apt update``` 

#untuk instal postgresql gunakan package contrib 
```sudo apt-get install postgresql postgresql-contrib```  

#verifikasi postgresql pada ubuntu
```sudo -u postgres psql -c "SELECT version();"```  

#untuk masuk ke postgresql
```sudo su - postgres```

```psql```

#untuk membuat password
```\password```

#untuk meriksa koneksi database
```\conninfo```

#untuk keluar
```\q```

#untuk membuat user
```createuser -interactive```

#membuat database
```createdb nama database```


