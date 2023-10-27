"""
Fonksiyonlar, belirli işlevleri olan ve tekrar tekrar kullanılan yapılardır.

Fonksiyonların metodlardan farkı, metodlar belli objelerin üzerinde uygulanırken fonksiyonlar tek başına da kullanılabilir.
ÖRN: print() fonksiyonu.

Fonksiyonlar bir defa tanımlanır ve ihtiyaç olunduğunda tekrar tekrar kullanılabilir.

Python geliştiricilerinin yazdığı ve hazır olarak kullandığımız print(), type() gibi fonksiyonlara built-in fonksiyonlar denir.

Ancak bunun haricinde biz kendi fonksiyonlarımızı da tanımlayabiliriz. Bunlara da user-defined fonksiyonlar denir.

Fonksiyonlar şu şekilde tanımlanır:

def fonksiyon_adi(parametre1,parametre2...):
    fonksiyon bloğu
    yapılacak işlemler
    dönüş değeri - opsiyonel

"""
# ÖRN:


def selamVer():  # fonksiyon tanımlandı
    print("Merhaba!")


selamVer()  # fonksiyonu kullanmak için çağırdık.

# Parametre alan bir fonksiyon tanımlayalım:


def selamla(isim):
    print("Hoşgeldin {}".format(isim))

# parametre alan fonksiyonumuzu çağıralım:


selamla("Feyza")


# FONKSİYONLARDA RETURN İFADESİ

# Bir fonksiyon tanımlandıktan sonra, bu fonksiyonun kullanımı sonucunda elde edilen değerler programların başka yerlerinde kullanılmak istenebilir.
# Bunu yapabilmek içinse return ifadesini kullanırız.

# return ifadesi, fonksiyonun işlemi bittikten sonra çağrıldığı yere değer döndürmesi anlamı taşır. Böylelikle, fonksiyonda aldığımız değeri bir değişkende depolayabilir ve değeri programın başka yerlerinde kullanabiliriz.

# ÖRN:

"""def topla(a,b,c):
    print("Toplamları: ",a+b+c)

def ikiyleCarp(a):
    print("İkiyle çarpımı: ",a*2)

toplam= topla(3,4,5)
ikiyleCarp(toplam)"""

# Böyle bir atama işlemi yaptığımızda kodumuz hata verir.
# Çünkü topla fonksiyonumuzda herhangi bir değer elde etmiyoruz yalnızca print fonksiyonuyla sonucumuzu ekrana yazdırıyoruz. Bu yüzden herhangi değer elde etmediğimiz için de bu fonksiyonun sonucunu başka bir fonksiyonda parametre olarak kullanamayız.

# Şimdi bunu bir de return ile yapalım.


def toplama(a, b, c):
    return a+b+c


def ikiyleCarp(a):
    return a*2


toplam = toplama(3, 4, 5)
print(ikiyleCarp(toplam))

# bu şekilde yaptığımızda ise toplama fonksiyonunun sonucu bir değer döndürür ve biz bu değeri başka bir fonksiyonda parametre olarak kullanabiliriz.


# return ifadesiyle ilgili bir diğer önemli şey de şudur:
# return ifadesi fonksiyonu tamamen bitirir. yani fonksiyon içerisinde return ifadesinden sonra tanımlanan hiç bir işlem çalışmaz ve fonksiyon sonlandırılır.

# FONKSİYONLARDA PARAMETRE TÜRLERİ

"""Parametre alan fonksiyonları parametre vermeden çağırmaya çalışırsak hata alırız. 
ÖRN:
"""


def selamVer(isim):
    print("Merhaba", isim)


selamVer()

"""Biz bu fonksiyonu bu şekilde içerisine bir parametre girmeden çağırmaya çalışırsak hata alırız.

Ancak eğer bu fonksiyona parametre verirken varsayılan bir değer verirsek;"""


def selamVer2(isim="İsimsiz"):
    print("Merhaba", isim)


selamVer2()

"""bu sefer bu fonksiyonu içerisine herhangi bir parametre vermeden çalıştırırsak, bize şu sonucu döndürür:

Merhaba İsimsiz

yine içerisinde bir değerle çağırırısak o değeri kullanarak işlem yapar.
#ÖRN:

selamVer2("Feyza")

bu şekilde çağırdığımızda ise

Merhaba Feyza

sonucunu ekranda görürürüz.

"""

# ESNEK SAYIDA DEĞERLER

"""Biz bir fonksiyon tanımlarken belirli sayıda parametre veriyoruz ve bu parametrelerden daha fazlasını fonksiyona gönderemeyiz.
ÖRN:
"""


def cikar(a, b):
    return a-b


cikar(1, 2, 3)

# Bu şekilde bi çağırmak işlemi yaptığımızda hata alırız.

"""
Eğer biz bir fonksiyonu tanımlarken parametrelerinin esnek olarak, yani belirli sayıda olmayacak şekilde gönderilebilmesini istiyorsak şu şekilde tanımlarız:

"""


def goster(*a):
    print(a)


goster(1, 2, 3, 4, 5)

# Bu şekilde çağırdığımızda bize sonuç olarak
# (1,2,3,4,5)
# sonucunu döndürür.

# Yani böylelikle bir fonksiyonu kaç tane parametre alacağını belirlemeden tanımlayabiliriz ve kullanırken de içinde istediğimiz kadar parametre gönderebiliriz.


# GLOBAL VE YEREL DEĞİŞKENLER

"""
Bir fonksiyon içerisinde tanımlanmış değişkene Yerel (local) değişken denir ve fonksiyon dışında herhangi bir yerden erişilemez.
Yerel değişkenler fonksiyon içerisinde üretildikten sonra fonksiyonun çalışması bittiği anda bu değişkenler de yok olur.

Fonksiyon dışında tanımlanan değişkenlere ise Global değişkenler denir ve bu değişkenlere programın her yerinden ulaşılabilir.

"""

# global ve lokal değişkenleri birlikte kullanalım:

c = 10


def func():
    c = 2
    print(c)


func()
print(c)

# Öncelikle bu kodun çıktısı şu şekilde olacaktır:

# 2
# 10

"""
Bunun sebebi ise şudur:
fonksiyon dışında global olarak bir c değişkeni tanımlandı ve 10 değeri atandı.
Daha sonrasında biz fonksiyon içerisinde başka bir c değeri tanımladık ve değerini de 2 olarak atadık.
fonksiyonu çağırdığımızda 2 değerini, ve fonksiyon dışında print fonksiyonu ile c değerini ekrana yazdırmak istediğimizde ise 10 değerini görürüz.

Ancak eğer biz, fonksiyon içerisinde yeni bir c değişkeni tanımlamak istemeyip de global olan c değişkenini kullanıp onun üzerinde işlem yapmak,     değerini değiştirmek istemiyorsak şu şekilde bir kullanım yaparız:

"""

d = 5


def function():
    global d
    d = 3
    print(d)


function()
print(d)

"""
Bu kodun sonucunda, global anahtar kelimesi sayesinde globalde oluşturulmuş d değişkeni üzerinden değişiklik yaparız. ve d değişkeninin yeni değeri 3 olur.
Dolayısıyla d değişkeninin değeri, fonksiyonun içinden çağrıldığında da dışından çağrıldığında da bize 3 değerini döndürür.

"""

# NOT:
"""
Herhangi bir if veya while döngüsü içerisinde tanımlanan değişkenler de global değişken olarak tanımlanır.
"""

# LAMBDA İFADELERİ

# tek bir satırda fonksiyon tanımlaması yapılabilir ve lambda ifadeleri ile kullanılabilir.

# etiket= lambda parametre1, parametre2... : işlem

# ÖRN:


def ucleCarp(x):  # normal fonksiyon tanımlaması
    return x*3

ucleCarp= lambda x : x*3 #lambda ifadesiyle tanımlanması

#lambda ifadeleri yalnızca az işlemli fonksiyonlarda kullanılır.
