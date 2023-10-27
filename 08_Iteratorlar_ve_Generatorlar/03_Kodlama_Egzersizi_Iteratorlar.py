"""
Iterable bir sınıf yapalım.
"""

class UcunKuvvetleri():
    def __init__(self,max=0):
        self.max=max
        self.kuvvet=0 #ilk olarak 3 ün 0. kuvvetini alalım.
    def __iter__(self):
        return self
    def __next__(self):
        #kuvvet değeri eğer maksimum kuvvet alma değerinden küçükse veya eşitse
        if(self.kuvvet<=self.max): 
            #max parametresi en fazla kaçıncı kuvvetini alacağımızı gösterir.
            sonuc=3**(self.kuvvet)
            #next metodunu her çağırdığımızda o anki kuvvet değeriyle 3'ün üssünü alıp sonuc değişkenine atayalım.
            self.kuvvet+=1
            #daha sonra kuvvet değerini 1 artıralım
            return sonuc
            #en son da bu sonuc değerini döndürelim.
        else:
            raise StopIteration
        
kuvvet=UcunKuvvetleri(6) #6 değeri 3'ün en fazla 6. kuvvetine kadar üs alma işlemi yapacağını belirliyor
iterator=iter(kuvvet) #bu satır yalnızca, değerleri tek tek next() metodu ile ekrana yazdıracağımız zaman gerekli.

for i in kuvvet:
    print(i)

"""
1
3
9
27
81
243
729
"""
print("1. for döngüsü:")
kuvvet=UcunKuvvetleri(6) #6 değeri 3'ün en fazla 6. kuvvetine kadar üs alma işlemi yapacağını belirliyor
#ayrı bir iterator objesi oluşturmadan da bunu elde edebiliriz.
#çünkü zaten for döngüsü next metodunu çalıştırıyor.
for i in kuvvet:
    print(i)

"""
1
3
9
27
81
243
729
"""

print("2. for döngüsü:")

for i in kuvvet:
    print(i)

"""
1. for döngüsü:
1
3
9
27
81
243
729
2. for döngüsü:
"""

#bunu yaptığımız zaman, nesnemizi yeniden üretmediğimiz sürece,
#iterator son elemanda kaldığı için döndürebileceği bir şey kalmadığından bu for döngüsü çalışmaz.
#bunun olmaması için, fonksiyon içerisinde StopIteration hatası aldığımız zamanki durumda,
#yani index sayısı verilerin en sonuna gelmiş olduğunda
#kuvvet değerini tekrar 0'a eşitleyebiliriz.
#Böylece baştan başlamış olur.

class UcunKuvvetleri():
    def __init__(self,max=0):
        self.max=max
        self.kuvvet=0 #ilk olarak 3 ün 0. kuvvetini alalım.
    def __iter__(self):
        return self
    def __next__(self):
        #kuvvet değeri eğer maksimum kuvvet alma değerinden küçükse veya eşitse
        if(self.kuvvet<=self.max): 
            #max parametresi en fazla kaçıncı kuvvetini alacağımızı gösterir.
            sonuc=3**(self.kuvvet)
            #next metodunu her çağırdığımızda o anki kuvvet değeriyle 3'ün üssünü alıp sonuc değişkenine atayalım.
            self.kuvvet+=1
            #daha sonra kuvvet değerini 1 artıralım
            return sonuc
            #en son da bu sonuc değerini döndürelim.
        else:
            self.kuvvet=0
            raise StopIteration


kuvvet=UcunKuvvetleri(6) 

print("1. for döngüsü:")

for i in kuvvet:
    print(i)

"""
1
3
9
27
81
243
729
"""

print("2. for döngüsü:")

for i in kuvvet:
    print(i)

"""
1. for döngüsü:
1
3
9
27
81
243
729
2. for döngüsü:
1
3
9
27
81
243
729
"""