
# args parametresi:

def fonksiyon (*args):
    # * burada bu fonksiyona istediğimiz kadar argüman gönderebileceğimizi simgeler.
    for i in args:
        print(i)

#Burada for döngüsü içerisinde, fonkiyona gönderdiğimiz parametreler
#demet haline çevrilecek ve bu demet içerisinde gezinip parametreleri ekrana yazdırabileceğiz.


fonksiyon(1,2,3)

#Ekranda 1,2,3 ifadelerini gördük.

# **kwargs parametresi:

# argümanlara isim vererek gönderebilmemizi sağlar.

def fonksiyon2(**kwargs):
    print(kwargs)

fonksiyon2(isim="Feyza",soyisim="Koç",numara=12345)

#{'isim': 'Feyza', 'soyisim': 'Koç', 'numara': 12345}

#kwargs parametresi bize bir sözlük yapısı döndürür.

def fonksiyon2(**kwargs):
    for i,j in kwargs.items():
        print("Argüman ismi:",i,"Argüman Değeri:",j)

fonksiyon2(isim="Feyza",soyisim="Koç",numara=12345)


"""
Argüman ismi: isim Argüman Değeri: Feyza
Argüman ismi: soyisim Argüman Değeri: Koç
Argüman ismi: numara Argüman Değeri: 12345
"""

def fonksiyon3(*args,**kwargs):
    for i in args:
        print(i)

    print("---------------")
    for i,j in kwargs.items():
        print(i,j)

fonksiyon3(1,2,3,4,5,6,isim="Feyza",soyisim="Koç",numara=12345)

"""
1
2
3
4
5
6
---------------
isim Feyza
soyisim Koç
numara 12345
"""

#İç İçe Fonksiyonlar:

#Fonksiyonlar da birer obje oldukları için hem bir değişkene atanabilirler,
#hem de başka bir fonksiyonun içinde tanımlanabilirler.

def selamla(isim):
    print("Merhaba",isim)

selamla("Feyza")
# Merhaba Feyza
#selamla fonksiyonunu başka bir değişkene atayabiliriz.

merhaba=selamla

#burada merhaba değişkeni de bir fonksiyon objesi ve fonksiyon olmuş olur.
#merhaba değişkeni artık selamla fonksiyonu gibi kullanılabilir.

merhaba("Kemal")
#Merhaba Kemal

#selamla fonksiyonunu silersek bile merhaba fonksiyonu silinmez.
#NOT: objeler del fonksiyonu ile silinir.

def fonksiyon4():
    def fonksiyon5():
        print("Alt fonksiyondan herkese merhaba")
    fonksiyon5()
    print("Üst fonksiyondan herkese merhaba")

fonksiyon4()

"""
Alt fonksiyondan herkese merhaba        
Üst fonksiyondan herkese merhaba 
"""

#fonksiyon4 içerisindeki fonksiyon5 lokal bir fonksiyon olduğu için,
#fonksiyon4 dışında herhangi bir yerden erişilemez.

def fonk(*args): #birden fazla parametre alan bir fonksiyon tanımlıyoruz.
    def toplama(demet): #demet olarak aldığımız parametreleri gönderdiğimiz ikinci bir fonksiyon tanımlıyoruz.
        toplam=0
        for i in demet:
            toplam+=i
        return toplam
    print(toplama(args)) #toplama fonksiyonunu içerisine args ile aldığımız demet halindeki parametreleri göndererek çağırıyoruz
    #ve print ile return ile dönen değeri ekrana yazdırıyoruz.
    

fonk(1,2,3,4,5,6)
# 21