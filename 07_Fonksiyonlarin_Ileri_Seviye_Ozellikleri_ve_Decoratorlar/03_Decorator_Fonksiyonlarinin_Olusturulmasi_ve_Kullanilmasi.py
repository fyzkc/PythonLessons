"""
Decorator fonksiyonlar, fonksiyonlarımıza dinamik olarak ekstra özellik eklediğimiz fonksiyonlardır.
Decorator fonksiyonların kullanımı kod tekrarını engeller.

"""

import time

def kareleriHesapla(sayilar):
    sonuc=list()
    baslama=time.time()
    for i in sayilar:
        sonuc.append(i**2)
    bitis=time.time()
    print("Fonksiyon süresi:",bitis-baslama)
    return sonuc
def kupleriHesapla(sayilar):
    sonuc=list()
    baslama=time.time()
    for i in sayilar:
        sonuc.append(i**3)
    bitis=time.time()
    print("Fonksiyon süresi:",bitis-baslama)
    return sonuc

#bu fonksiyonların içindeki for döngülerinin ne kadar süre aldığını öğrenmek istersek,
#öncelikle time modülünü import etmemiz gerekir.

#bunun için öncelikle başlangıç zamanını anlamak için time.time() bu kodu kullanırız.
#burada time() fonksiyonu şimdiki zamanı bize saniye cinsinden verir.

#bitiş zamanı için de aynı işlemi yapıyoruz ve aradaki farkı görebilmek ve toplam kaç saniye işlem
#yapıldığını anlayabilmek için bitiş zamanından başlangıç zamanını çıkartıyoruz ve ekrana yazdırıyoruz.

kareleriHesapla(range(100000)) 
#0 dan 100000 e kadar olan sayıların karelerini hesaplayacak.

kupleriHesapla(range(100000))
#0 dan 100000 e kadar olan sayıların küplerini hesaplayacak.

"""
İlk fonksiyon için:
Fonksiyon süresi: 0.009974241256713867
İkinci fonksiyon için:
Fonksiyon süresi: 0.012964010238647461

"""

#burada görüldüğü gibi bu zaman hesabını biz ikinci fonksiyonumuzda tekrar yazdık.
#yani kod tekrarı oldu.
#ayrıca bu fonksiyonlarımızın görevi zaman hesaplamak değil.
#fonksiyonları sadece tek bir iş yapacak şekilde kullanmamız gerekiyor.
#bu yüzden buradaki zaman hesaplama işlemini decorator fonksiyonları sayesinde yapmaya çalışalım.

def zamanHesapla(func):
    def wrapper(sayilar):
        baslama=time.time()
        sonuc=func(sayilar)
        bitis=time.time()
        print(func.__name__ + " " + str(bitis-baslama) + "Saniye sürdü.")
        return sonuc
    return wrapper

"""
Zaman hesapla decorator fonksiyonu şu şekilde çalışıyor:
Öncelikle biz içerisine fonksiyon parametresi alan bir zamanhesapla fonksiyonu tanımlıyoruz.
Daha sonra bu fonksiyon içerisinde bir sayi dizisi alan başka bir fonksiyon tanımlıyoruz.
bu fonksiyonun içinde öncelikle, başta parametre olarak verdiğimiz fonksiyonu çağırmadan önce, başlangıç zamanını baslama isimli bir değişken ile alıyoruz.
daha sonra başta parametre olarak gönderdiğimiz fonksiyonu, ikinci fonksiyona veridğimiz sayi listesini parametre olarak verip çağırıyoruz.
ve bu fonksiyodan dönen sonucu da sonuc isimli bir fonksiyona atıyoruz.
fonksiyonumuzun çalışması bittikten sonra da bitiş zamanını alıyoruz.
sonuc değerini döndürmeden önce, ekrana fonksiyonun çalışma süresini yazdırıyoruz.
daha sonra da fonksiyonumuzun sonuc değerini return ile döndürüyoruz.
en son ise ilk fonksiyon içine yazdığımız alt fonksiyonun çalışması için return ile bu fonksiyonu döndürüyoruz.

Bu artık bizim decorator olarak kullanacağımız fonksiyonumuz oluyor.
Buradaki amacımız, belirli bir işlem yapan bi fonksiyonumuz varken, bu fonksiyon içerisinde amacında farklı olarak
başka işler de yaptırmak istersek, bu fonksiyon içerisinde bunları yazmamamız.
Çünkü bu şekilde fonksiyon kendi amacından şaşmış olacak.
Ayrıca birden fazla yerde aynı kodu tekrarlamak zorunda kalmış olacağız.

Bunun için ekstra yaptırmak istediğimiz işlemleri başka bir fonksiyon içerisinde yazıp,
bu fonksiyonu da asıl fonksiyonlarımıza dinamik olarak ekliyoruz.

Bu fonksiyonları diğer fonksiyonlara ekleyebilmek için, eklemek istediğimiz fonksiyonun üzerine
@ işareti ile bu fonksiyonun adını yazıyoruz.

"""


@zamanHesapla
def kareleriHesapla(sayilar):
    sonuc=list()
    for i in sayilar:
        sonuc.append(i**2)
    return sonuc

@zamanHesapla
def kupleriHesapla(sayilar):
    sonuc=list()
    for i in sayilar:
        sonuc.append(i**3)
    return sonuc

kareleriHesapla(range(100000))

kupleriHesapla(range(100000))

"""
kareleriHesapla 0.010991811752319336Saniye sürdü.
kupleriHesapla 0.013902664184570312Saniye sürdü.
"""

#NOT: Asıl istenen sonuç olan sayıların kareleri ve küplerini yazdırma işlemini yapmadık.
#Çok uzun bir sonuç elde edildiği için. 
#Ancak print() ile fonksiyonumuzu çalıştırırsak bu sonucu da elde ederiz.
#Yani bu kısım çalışmıyor değil. 

