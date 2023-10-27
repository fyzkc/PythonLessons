"""
sys modülü bizim sistemimizde kurulu olan Python sürümünü
yönetiiğimiz standart bir modüldür.
Bu modülü kullanarak Python sistemine özgü fonksiyonları 
ve özellikleri kullanabiliriz.
"""
import sys

#exit(): programın sona erdirilmesini sağlar.

# a=input("a: ")
# b=input("b: ")

# sys.exit()

# c=input("c: ")

# a: 1
# b: 2

#exit() fonksiyonundan sonraki hiç bir koda erişilemez.
#O yüzden onu örnek olarak gördükten sonra yorum satırı haline getiriyorum.

#stderr() ve stdout():
#Bilgisayarlar uygulamalarımız ve işlemlerimiz çalıştığı zaman
#çıktı vermek ve girdi almak için şu dosyaları kullanır:

#stdin: Bu standart dosya, işlemimizin kullanıcıdan input almasını sağlar.
#stdout: Bu standart dosya, işlemimizin çıktı vermesini sağlar.
#stderr: Bu standart dosya, işlemimizin hata mesajlarını çıktı olarak vermesini sağlar.

#stderr dosyasına kendimiz bir şeyler yazabiliriz:

sys.stderr.write("Bu bir hata mesajıdır\n")
#Böyle bir şey yaptığımızda, bu hata mesajı bir buffer'ın içerisine gidiyor.
#Ve buffer, ekrana bir şey yazdırmak için şu işlemi bekler:

sys.stderr.flush()

#Aslında flash() fonksiyonunu kullanmadan da ekrana yazdırabiliriz ama
#Büyük dosyalarda buffer'a yazdığımız bir şeyi anında ekrana yazdırmak için
#bu fonksiyonu kullanıyoruz.
#Bu fonksiyon buffer'ı boşaltarak ekrana çıktı olarak verir.

#Bu bir hata mesajıdır

#argv: Programımızı komut satırı üzerinden çalıştırdığımız zaman,
#komut satırından kullanıcıdan değer alma işlemini bu özellik sayesinde gerçekleştirebiliriz.

print(sys.argv)
# ['c:/Users/Feyza/Desktop/Python Dersleri/9-Ileri Seviye Modüller/4-Sys Modülü.py']

#Komut satırından herhangi bir parametre girdiğimiz zaman,
#bu parametreler yukarıda çıktı verilen listeye tek tek eklenir.
#Biz de bunları alıp programlarımıza yazabiliyoruz.

for i in sys.argv:
    print(i)

#Bu dosyayı terminalden çalıştırmamız gerekiyor.

# python C:\Users\Feyza\Desktop\Python_Dersleri\9_Ileri_Seviye_Moduller\4_Sys_Modulu.py 1 2 3 4 5

#Burada dosyayı python komutu ile çalıştırıyoruz. Daha sonra çalıştıracağımız dosyayı yazıyoruz.
#Çalıştıracağımız dosyayı da yazdıktan sonra klavye üzerinden değerler giriyoruz.

#NOT: Dosyanın tam yolunu vermeden çalışmıyor.

def kokBulma(a,b,c):
    delta = (b**2) - (4*a*c)

    if(delta<0):
        print("Reel kök yok")
    else:
        x1= ((-b) - (delta**0.5))/(2*a)
        x2= ((-b) + (delta**0.5))/(2*a)
        return (x1,x2)
    
if(len(sys.argv)==4):
    print(kokBulma(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
    #Burada kökbulma fonksiyonumuzu terminalden girilen değerlere göre çalıştırmak için,
    #fonksiyonumuzun parametrelerini sys.argv ile terminal ekranından alıyoruz.
    #Burada, terminal ekranımızda, ekran çıktısı olarak bir liste döner.
    #Bu listenin ilk elemanı yani 0. indexi dosyanın konumu ve sırasıyla diğerleri de girilen değerler olur.
    #O yüzden sys.argv listemizin 1. indexinden sonrası bizim terminal ekranından girdiğimiz değerlerdir.
    #Sırasıyla onları alarak kokBulma fonksiyonumuza gönderip fonksiyonumuzu çalıştırıyoruz.

else:
    sys.stderr.write("Lütfen yalnızca 3 tane değer girin.")
    sys.stderr.flush()

# 1 2 1 değerleri için:
# (-1.0, -1.0)

