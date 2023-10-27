"""
SQLite veritabanı, diğer veritabanlarında olduğu gibi sunucu kurmayı gerektirmez.
Yani sunucusuz bir veri tabanıdır.
Herhangi bir programın yanına sqlite veritabanı kurulabilir.

Sqlite veritabanında işlemler yaptıktan sonra veritabanını incelemek için
'sqlite browser' kullanacağız.

"""

# SQLite Veritabanı Oluşturma

import sqlite3

#Kütüphane.db isimli veritabanını oluşturup bağlanmak için:
con = sqlite3.connect("Kütüphane.db") 
#Eğer böylr bir veritabanı varsa sadece bağlanır.

cursor= con.cursor()
#Bir imleç oluşturup cursor değişkenine atadık.
#Database üzerindeki bütün işlemleri bu değişkenle gerçekleştirebiliriz.

#Cursor'lar bir veri grubu (tablo) üzerinde satır satır işlem yapabilmeyi sağlar . 
#Bir nevi for döngüsü gibi çalışır , belirtilen select sorgusundan gelen verileri satır satır döndürür 
#ve cursor içinde tanımlanan işlemi yapar.

#Veritabanıyla işimiz bittiğinde bağlantıyı kapatmamız gerekiyor.
#con.close()

# SQLite Tablo Oluşturma

#Veritabanında 'Kitaplık' isimli bir tablo oluşturmak için iki farklı sorgu kullanabiliriz:

# CREATE TABLE Kitaplık(İsim TEXT, Yazar TEXT, Yayınevi TEXT, SayfaSayisi INT)
#Bu sorgu kitaplık isimli bir tablo oluşturur ve bu tablonun özellikleri verildiği gibi olur.
#Ancak bu tabloyu birden fazla çalıştırırsak Table Already Exists hatası alırız.

# CREAT TABLE IF NOT EXISTS Kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, SayfaSayisi INT)
#Bu sorgu bu isimde bir tablo yoksa oluşturur, tavlo zaten varsa herhangi bir işlem yapmaz.

def tabloOlustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, SayfaSayisi INT)")
    #execute() fonksiyonu sorgu çalıştırmak için kullanılır.
    con.commit()
    #execute fonksiyonu sorguyu çalıştırır ancak veritabanında bu sorgunun etkili olması için
    #commit fonksiyonunu çalıştırmamız gerekir

tabloOlustur()

con.close()