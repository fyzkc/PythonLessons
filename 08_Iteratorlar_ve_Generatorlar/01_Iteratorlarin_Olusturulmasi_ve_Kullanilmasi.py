"""
Iteratorler, özellikle döngülerde, list comprehensionda ve 
generatorlarda karşımıza çıkar.

Iteratorler en genel anlamıyla üzerinde gezinilebilecek
bir objedir ve bu obje her seferinde bir tane eleman döner.

Kendisinden iterator oluşturulabilecek olan her obje iterable bir objedir.
Örn. demetler, listeler ve stringle iterable objelerdir.

Bir objenin iterable olması için hazır metotlar olan
__iter__() ve __next__() metotlarının tanımlanması gerekir.

"""

#Iterator Oluşturma

"""
Bir iterator objesini iterable bir objeden oluşturmak için
Pyhtonda iter() fonksiyonunu kullanıyoruz ve bu objenin
bir sonraki elemanını almak için next() fonksiyonunu kullanıyoruz.

"""

liste=[1,2,3,4,5]
iterator = iter(liste)
print(iterator)
#<list_iterator object at 0x000001867E4E9600>
#iterator objemiz bu şekilde oluştu.
#elemanlara erişebilmek için de next() fonksiyonunu kullanmamız gerekiyor.

print("----------------------")


print(next(iterator))
# 1
print(next(iterator))
# 2

print("----------------------")

#eleman bittiğinde next fonksiyonu hata verir.

for i in liste:
    print(i)


print("----------------------")

#yukarıdaki işlemin aslında python tarafından nasıl çalıştığına bakalım:

iterator=iter(liste)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

#yani aslında for döngüsü de bir nevi iterator ile yazılmış diyebiliriz.

# Kendi Iterator Objelerimizi Oluşturmak

#Kendi itaretor objelerimizi oluşturabilmek için,
#oluşturacağımız sınıf içerisinde mutlaka __iter__() ve __next__()
#fonksiyonlarını tanımlamamız gerekiyor.

class Kumanda():
    def __init__(self,kanalListesi):
        self.kanalListesi=kanalListesi
        self.index=-1
    def __iter__(self):
        return self
        #iter fonksiyonu interator objesi oluşturabilmek için vardır.
        #return self dediğimiz zaman direkt olarak bu fonksiyonun kendisinden
        #iterator oluşturmuş oluruz.
    def __next__(self):
        self.index+=1
        #next fonksiyonunu her çağırdığımızda index değeri bir artacak.
        if(self.index<len(self.kanalListesi)):
            return self.kanalListesi[self.index]
            #eğer index değeri objenin uzunluğundan fazla değilse,
            #objenin o index değerindeki değeri return edilecek.
        else:
            self.index=-1
            raise StopIteration
            #değilse index değeri tekrar -1 olarak atanıp StopIteration hatası fırlatılacak.

kumanda=Kumanda(["ATV","TRT","FOX","Kanal D","Show TV"])
iterator=iter(kumanda)
#burada kumanda objesini iter fonksiyonuna gönderdiğimizde,
#Kumanda sınıfındaki __iter__() fonksiyonu çalışır.
#bu fonksiyonun içerisinde de return self dediğimiz için,
#bu fonksiyon kumanda objesinin kendisini return eder.
#dolayısıyla da return edilen bu kumanda objesi, artık bir iterator olarak
#iterator değişkenine atanır.

print(next(iterator))
#ATV
print(next(iterator))
#TRT
print(next(iterator))
#FOX
print(next(iterator))
#Kanal D
print(next(iterator))
#Show TV
#print(next(iterator))


# Traceback (most recent call last):
#   File "c:\Users\Feyza\Desktop\Python Dersleri\8-Iteratorlar ve Generatorlar\Iteratorların Oluşturulması ve Kullanılması.py", line 108, in <module>
#     print(next(iterator))
#           ^^^^^^^^^^^^^^
#   File "c:\Users\Feyza\Desktop\Python Dersleri\8-Iteratorlar ve Generatorlar\Iteratorların Oluşturulması ve Kullanılması.py", line 86, in __next__
#     raise StopIteration
# StopIteration 

kumanda=Kumanda(["ATV","TRT","FOX","Kanal D","Show TV"])
iterator=iter(kumanda)
#yeniden tanımlamamın sebebi, yukarıda next metoduyla iterasyonu sona getirdiğim için
#baştan başlaması gerekiyor.
#o yüzden tekrar tanımlayıp for döngüsüyle içinde gezmeyi görebiliyorum.

for i in kumanda:
    print(i)


"""
ATV
TRT
FOX
Kanal D
Show TV
"""
