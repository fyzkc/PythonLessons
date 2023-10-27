"""
Python'da bir dosya otomatik olarak nasıl kapatılır?
"""

# with open(dosyaAdi,dosyaAcmaKipi) as file:
#     Dosya işlemleri

#Bu şekilde bu with open as file bloğu içerisinde biz dosya işlemlerimizi gerçekleştirebilir,
#işimiz bittiğinde de otomatik olarak kapatılmış olmasını sağlayabiliriz.


#Bir dosyadan okuma yaparken open() fonksiyonu ile açtığımız dosyayı
#bir file değişkenine atayıp, file.read() şeklinde okuma yapıyorduk.
#Ancak bu şekilde okuma yaparken, file değişkeni bir imleç gibi davranır.
#Yani dosya içerisinde en son nereyi okuduysa ordan devam ederek okuma yapar.
#Ancak biz dosya okuma yaparken imleci dosyanın herhangi bir yerine götürmeyi
#isteyebiliriz.
#Bunun için seek() fonksiyonunu kullanacağız. Ve imlecin nerde olduğunu görebilmek için de
#tell() fonksiyonunu kullanacağız. Bu fonksiyon bize dosya imlecinin hangi byte'ta olduğunu söyler.

with open("C:/Users/Feyza/Desktop/Python Dersleri/3-Dosya Islemleri/bilgiler.txt","r",encoding="utf-8") as file:
    print(file.tell())

#Bu kodu çalıştırdığımızda 0 değerini ekranda görürüz. Bu bize file değişkeninin
#dosyanın 0. byte'ı üzerinde olduğunu gösterir.


with open("C:/Users/Feyza/Desktop/Python Dersleri/3-Dosya Islemleri/bilgiler.txt","r",encoding="utf-8") as file:
    file.seek(20)
    print(file.tell())

#Bu kodun çıktısı da 20 olacaktır. Yani file değişkeninin dosyanın 20. byte'ına gittiğini gösterir.

#NOT: 20. byte'a gitmesi demek 20. karakter üzerinde olması anlamına gelir.
#Dosyalar içerisindeki her bir karakter 1 byte yer kaplar.

with open("C:/Users/Feyza/Desktop/Python Dersleri/3-Dosya Islemleri/bilgiler.txt","r",encoding="utf-8") as file:
    file.seek(5)
    icerik=file.read(10)
    print(icerik)

#read() fonksiyonunu bu şekilde içine bir değer göndererek kullandığımızda, girdiğimiz değer kadar karakter okur.

#Yukarıdaki kod, öncelikle dosya değişkenini 5. karaktere gönderir. Daha sonra da 5. karakterden sonra gelen 10 karakteri okuma işlemi yapar.
