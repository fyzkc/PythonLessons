"""
Os modülü işletim sisteminde işlemler gerçekleştirebildiğimiz standart bir Python modülüdür.
"""
from datetime import datetime
import os

#getcwd(): Bulunduğumuz dizini gösteren fonksiyon

print(os.getcwd())
#C:\Users\Feyza\Desktop\Python Dersleri

#os.chdir(""): Bir dosyanın var olan konumundan başka bir konuma
#taşınması için kullanılan fonksiyon. Parantez içerisine,
#taşımak istediğimiz dizini yazıyoruz.

#listdir(): Bulunulan dizindeki dosyaları ve klasörleri listeler.

print(os.listdir())

# [
# '1-Başlangıç Konuları', 
# '2-Nesneye Dayalı Programlama', 
# '3-Dosya Islemleri', 
# '4-Pythondaki Gömülü Fonksiyonlar.py', 
# '5-Ileri Seviye Veri Yapıları ve Objeler', 
# '6-Sqlite Veritabanı', 
# '7-Fonksiyonların Ileri Seviye Ozellikleri ve Decoratorlar', 
# '8-Iteratorlar ve Generatorlar', 
# '9-Ileri Seviye Modüller'
# ]

#daha güzel görüntülemek için:

for i in os.listdir():
    print(i)

# 1-Başlangıç Konuları
# 2-Nesneye Dayalı Programlama
# 3-Dosya Islemleri
# 4-Pythondaki Gömülü Fonksiyonlar.py
# 5-Ileri Seviye Veri Yapıları ve Objeler
# 6-Sqlite Veritabanı
# 7-Fonksiyonların Ileri Seviye Ozellikleri ve Decoratorlar     
# 8-Iteratorlar ve Generatorlar
# 9-Ileri Seviye Modüller

#mkdir(): Bulunulan dizin içerisinde klasör oluşturmayı sağlar.
#Bu fonksiyonla iç içe iki tane klasörü aynı anda "Klasör1/Klasör2" şeklinde oluşturamayız.
#Bunu yapmak için:

#mkdirs() fonksiyonu kullanılır.

#rmdir(): Klasörü silmek için kullanılır.
#rmdir("Klasör1/Klasör2"): Klasör2'yi siler.
#rmdir("Klasör1"): Klasör1 silinir.

#("Klasör1/Klasör2") burada hem Klasör1'i hem de Klasör2'yi silmek için:
#rmdirs() fonksiyonu kullanılır.

#rename("dosyaadı","yenidosyaadı"): Bir dosyanın ismini değiştirmek için kullanılır.

#stat("dosya"): İçerisine verilen dosyaların bütün özelliklerini döner.
print(os.stat("C:/Users/Feyza/Desktop/Python Dersleri/9-Ileri Seviye Modüller/2- Os Modülü.py"))

# os.stat_result(st_mode=33206, 
# st_ino=7036874417781779, 
# st_dev=4175321418, 
# st_nlink=1, 
# st_uid=0, 
# st_gid=0, 
# st_size=2048, 
# st_atime=1691942961, 
# st_mtime=1691942961, : dosyanın değiştirilme zamanının saniye cinsinden değeri
# st_ctime=1691941538)

print(os.stat("C:/Users/Feyza/Desktop/Python Dersleri/9-Ileri Seviye Modüller/2- Os Modülü.py").st_mtime)
#1691943053.4016473

zaman=datetime.fromtimestamp(os.stat("C:/Users/Feyza/Desktop/Python Dersleri/9-Ileri Seviye Modüller/2- Os Modülü.py").st_mtime)
print(zaman)
#2023-08-13 19:12:01.579764

#Bu şekilde saniyeyi tarihe çevirerek dosyanın değiştirilme tarihine erişebiliriz.

#walk(): Belirli bir dizin altındaki bütün klasörlerin ve dosyaların özelliklerini demet olarak döndürür.
print("--------------")
print(os.walk("C:/Users/Feyza/Desktop"))
#<generator object _walk at 0x000001FA0EC44320>

#walk() fonksiyonu bir generator objesi döndürür.
#o halde içindeki elemanlara erişmek için bir for döngüsü kullanabiliriz.

print("--------------")
for i in os.walk("C:/Users/Feyza/Desktop"):
    print(i)

#Bütün dosyalar
# ('C:/Users/Feyza/Desktop', ['Projelerim', 'Python Dersleri'], ['desktop apps.txt', 'desktop.ini', 'diziler.txt', 'çeviri.png'])   
# ('C:/Users/Feyza/Desktop\\Projelerim', ['DiaryApp', 'Gömülü Sistemler Proje', 'HotelResepsiyon', 'KafeOtomasyonu', 'KitapSatisSayfasi', 'Yurt Otomasyonu'], [])
# ('C:/Users/Feyza/Desktop\\Projelerim\\DiaryApp', ['.vs', 'DiaryApp', 'resimler'], ['Diary-icon.png', 'DiaryApp.sln', 'VeriTabanı.mdf', 'VeriTabanı_log.ldf'])
# ('C:/Users/Feyza/Desktop\\Projelerim\\DiaryApp\\.vs', ['DiaryApp'], [])
# ('C:/Users/Feyza/Desktop\\Projelerim\\DiaryApp\\.vs\\DiaryApp', ['FileContentIndex', 'v16', 'v17'], [])
# ('C:/Users/Feyza/Desktop\\Projelerim\\DiaryApp\\.vs\\DiaryApp\\FileContentIndex', ['merges'], ['6cf359bf-1d79-46f0-9ee6-ef2fe5b0d039.vsidx'])
# ('C:/Users/Feyza/Desktop\\Projelerim\\DiaryApp\\.vs\\DiaryApp\\FileContentIndex\\merges', [], [])
# ('C:/Users/Feyza/Desktop\\Projelerim\\DiaryApp\\.vs\\DiaryApp\\v16', ['Server'], ['.suo'])
# ('C:/Users/Feyza/Desktop\\Projelerim\\DiaryApp\\.vs\\DiaryApp\\v16\\Server', ['sqlite3'], [])
# .....
#bu şekilde devam eder.

#Bunları daha anlaşılır olarak listelemek için:

for klasorYolu,klasorIsimleri,dosyaIsimleri in os.walk("C:/Users/Feyza/Desktop"):
    print("Klasör Yolu:",klasorYolu)
    print("Klasör İsimleri:",klasorIsimleri)
    print("Dosya İsimleri:",dosyaIsimleri)
    print("-------------------------------------")

#Buna benzer sıralanır:

# Klasör Yolu: C:/Users/Feyza/Desktop\Projelerim\HotelResepsiyon\HotelResepsiyon\obj\Debug\TempPE
# Klasör İsimleri: []
# Dosya İsimleri: []
# -------------------------------------
# Klasör Yolu: C:/Users/Feyza/Desktop\Projelerim\HotelResepsiyon\HotelResepsiyon\Properties
# Klasör İsimleri: []
# Dosya İsimleri: ['AssemblyInfo.cs', 'Resources.Designer.cs', 'Resources.resx', 'Settings.Designer.cs', 'Settings.settings'] 
# ......


#Yalnızca dosya isimlerini almak istersek:

for klasorYolu,klasorIsimleri,dosyaIsimleri in os.walk("C:/Users/Feyza/Desktop"):
    for i in dosyaIsimleri:
        print(i)

# desktop apps.txt
# desktop.ini
# diziler.txt
# çeviri.png
# Diary-icon.png
# DiaryApp.sln
# VeriTabanı.mdf
# VeriTabanı_log.ldf
# 6cf359bf-1d79-46f0-9ee6-ef2fe5b0d039.vsidx
# .suo
# storage.ide
# .suo
# App.config
# DiaryApp.csproj
# Form1.cs
# Form1.Designer.cs
# Form1.resx
# Form2.cs
# Form2.Designer.cs
# Form2.resx
# Form3.cs
# Form3.Designer.cs
# Form3.resx
# Program.cs
# DiaryApp.exe
# DiaryApp.exe.config
# DiaryApp.pdb
# ...

#Sadece txt uzantılı dosyaları almak istersek:

for klasorYolu,klasorIsimleri,dosyaIsimleri in os.walk("C:/Users/Feyza/Desktop"):
    for i in dosyaIsimleri:
        if(i.endswith(".txt")):
            print(i)

# desktop apps.txt
# diziler.txt
# DiaryApp.csproj.FileListAbsolute.txt
# HotelResepsiyon.csproj.FileListAbsolute.txt
# Veri tabanı dosyasını açma.txt
# KafeOtomasyonu.csproj.FileListAbsolute.txt
# about_EntityFramework6.help.txt
# KafeOtomasyonu.csproj.FileListAbsolute.txt
# about_EntityFramework6.help.txt
# KitapSatisSayfasi.csproj.FileListAbsolute.txt
# YurtOtomasyonu.txt
# YurtOtomasyon.csproj.FileListAbsolute.txt
# Beşiktaş.txt
# bilgiler.txt
# Fenerbahçe.txt
# futbolcular.txt
# Galatasaray.txt
# Gecenler.txt
# Kalanlar.txt
# Notlar.txt
# Ortalamalar.txt
# mailler.txt
# metin.txt
# Onuncu Ödev - siir.txt