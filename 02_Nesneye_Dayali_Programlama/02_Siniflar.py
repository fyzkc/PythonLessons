"""
Class anahtar kelimesi pythonda sınıfları üretmek için kullanılır.
Sınıflar, üreteceğimiz nesnelerin özelliklerini ve metotlarını tanımladığımız yapılardır.
"""

#ÖRN:

class Araba():  #burada Araba isminde bir veri tipi üreteceğimizi söylüyoruz.
    #araba sınıfımızdaki özellikleri tanımlayalım.
    #bu özelliklerin her biri, daha sonra bu araba sınıfı üzerinden bir obje oluştururken bu objeye yüklenecekler.
    model= "Renault Megan"
    renk = "Gümüş"
    beygirGucu= 110
    silindirSayisi= 4


#NOT: Sınıflardan obje türetmeyi şu şekilde düşünebiliriz:

"""
örneğin bizim integer adında bir veri tipimiz var. Ve biz bu int veri tipini kullanarak
çok sayıda farklı isimde değişken tanımlayabiliyoruz.
Ve tanımladığımız bu değişkenlerin her birine şnt veri tipinin özellikleri yükleniyor.
Örneğin int veri tipinin özelliği tam sayı olması ise, int veri tipi üzerinden tanımladığımız her bir 
değişkene de tam sayı olma özelliği yüklenir.

Benzer şekilde biz bir class oluşturduğumuz zaman, 
Örn. Araba isminde bir sınıf oluşturduk. Bu sınıfımızı bir veri tipi olarak düşünürüz.
Araba ismindeki veri tipinden bir değişken tanımlamak istediğimizde, işte bu da nesne olmuş olur.
Bu Araba veri tipindeki nesnelerin her birine Araba veri tipinin özellikleri ve metotları yüklenir.

"""

# Nesne Türetme:

araba1= Araba()  #araba1 isimli değişkeni Araba veri tipinden türetmiş olduk. burada araba1 bizim nesnemiz.
print(araba1.model)
#bu kod çalıştığında ekran çıktısı olarak:

#Renault Megan

#sonucunu alırız.

araba2 = Araba() #bu da ikinci Araba sınıfı nesnesi.

print(araba2.model)

#Bu kodun çıktısı da Renault Megan olacaktır.

#İki ayrı nesne üretmemize rağmen ikisinin de özellikleri aynı.

"""
Bir class oluştururken içerisine yazdığımız özellikler, daha sonra türetilecek olan nesnelere özel olmuyor.
Bu özellikler zaten class ın kendisine ait özellikler olduğundan kaç tane nesne üretirsek üretelim, ürettiğimiz
nesneler de bu özelliklerin aynılarına sahip oluyorlar.

Dolayısıyla eğer biz bu classlardan nesneler türetmeden de bu özelliklere erişebiliriz.

"""

print(Araba.model)

#Bu kodun çıktısı da yine Renault Megan olacaktır.

#Peki farklı değerlerle nesneler üretmek istiyorsak ne yapmamız gerekir?

#Bunun için __init__() fonksiyonunu kullanacağız.

#   __init__() fonksiyonu:

"""
Bu fonksiyon bir nesne oluşturulduğu zaman default olarak o nesneye yüklenir.
Eğer bu fonksiyonu kendimiz tanımlamazsak Python tarafından bu fonksiyon varsayılan olarak tanımlanır.
Ancak eğer herhangi bir class içerisinde biz bu fonksiyonu kendimiz tanımlarsak, default olarak tanımlanmaz.
Bu şekilde bu fonksiyonu kendimiz tanımlayarak kendi nesnelerimizi farklı değerlerle üretebiliriz.


__init__() fonksiyonu Pythonda yapıcı (constructor) bir fonksiyondur. Yani bu fonksiyon objeler oluşturulurken otomatik olarak
ilk çağrılan fonksiyondur. Bu fonksiyonun özel olarak çağrılması gerekmez. Nesneler oluşturulurken otomatik olarak çağrılır.

"""

class Araba(): # Araba classını tekrardan tanımlayalım.
    model= "Renault Megan"
    renk = "Gümüş"
    beygirGucu= 110
    silindirSayisi= 4

    def __init__(self):
        print("init fonksiyonu çağrıldı.")

araba1 = Araba()

#Bu şekilde Araba classından araba1 isimli bir nesne ürettiğimiz zaman 
#ekranda "init fonksiyonu çağrıldı" yazısı görülür.
#Bu demek oluyor ki bu fonksiyon, bir nesne üretildiği zaman otomatik olarak çağrılır.

#init fonksiyonunun parantezleri arasındaki self kelimesinin anlamı ise şudur:

#self anahtar kelimesi objeyi oluşturduğumuz zaman o objeyi gösteren bir referanstır.
#bu referansın mutlaka her bir metodun en başında bulunması gerekir.

class Araba(): # Araba classını tekrardan tanımlayalım.
    def __init__(self,model,renk,beygirGucu,silindir):
        self.model = model
        self.renk=renk
        self.beygirGucu=beygirGucu
        self.silindir=silindir

araba1= Araba("Renault Megan","Gümüş",110,4)
araba2=Araba("Peugeot","Beyaz",90,4)

# NOT: Objeyi oluştururken parametreler arasındaki self parametresini yazmamız gerekmiyor, o otomatik olarak atanıyor.

print(araba1.model)
#Renault Megan
print(araba2.model)
#Peugeot

#Parametrelere varsayılan değer de verilebilir. Nesne oluşturulurken parametrelere belli değerler atanmazsa
#bu varsayılan değerler kullanılır.

class Araba(): # Araba classını tekrardan tanımlayalım.
    def __init__(self,model="Bilgi Yok",renk="Bilgi Yok",beygirGucu=70,silindir=4):
        self.model = model
        self.renk=renk
        self.beygirGucu=beygirGucu
        self.silindir=silindir


araba= Araba(beygirGucu=110)

print(araba.model,araba.renk,araba.beygirGucu,araba.silindir)

#Bu şekilde model, renl ve silindir parametreleri varsayılan değerlerle gelirken beygirGucu parametresi bizim verdiğimiz değeri alır.


