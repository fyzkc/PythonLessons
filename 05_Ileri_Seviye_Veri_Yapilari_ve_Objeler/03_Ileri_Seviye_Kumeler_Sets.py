"""
Kümeler: matematikte olduğu gibi bir elemandan sadece bir tane tutan bir veritipidir.
"""

#Küme (set) tanımlama:

x={1,2,3}

print(type(x))
# <class 'set'> sonucu çıkar

#Boş küme:

x= set()

#Bir listedeki elemanları kümeye atayalım:

liste= [1,2,3,1,2,3,3,2,2,2,1,1]
x=set(liste)
print(x)

# {1, 2, 3} sonucu çıkar.
#Yani her elemanı yalnızca bir kere yazar.

#Kümeler üzerinde listelerde olduğu gibi for döngüsü ile gezinebilir:

x= {"Elma","Armut","Muz","Kiraz"}

for i in x:
    print(i)

# Kiraz
# Armut
# Muz
# Elma 
# sonucu çıkar.

#NOT: Görüldüğü gibi kümelerde herhangi bir eleman sırası yoktur.

print("----------------------")
x= {"Elma","Armut","Muz","Kiraz","Kiraz"}

for i in x:
    print(i)

# Armut
# Kiraz
# Muz
# Elma
#sonucunu alırız.

#NOT: Kiraz kelimesinden iki tane olmasına rağmen gezinirken yalnızca bir tanesini ekrana yazdırdı.

#Kümelerin elemanlarına direkt olarak erişebilir miyiz?

x= {"Elma","Armut","Muz","Kiraz"}

#x[0] 
#bu ifade hata verecektir.
#kümeler indexlerle çalışmaz.

#x["Elma"]
#bu ifade de hata verir.

#Kümelerin elemanlarını ya yukarıda yaptığımız gibi for döngüsü ile bastırırız,
#ya da kümeyi bir listeye çevirip o şekilde erişiriz.

liste=list(x)
print(liste)

#Kümelerin metotları:

#add(): Kümeye eleman eklemeyi sağlar. Aynı eleman eklenmeye çalışıldığında herhangi bir
#hata vermez ama ekleme işlemi de yapmaz. Çünkü kümelerde bir eleman sadece bir kere yazılır.

#difference(): Birinci kümenin ikinci kümeden farkını döndürür.

kume1= {1,2,3,10,34,100,-2}
kume2= {1,2,23,34,-1}

print(kume1.difference(kume2))
#{10, 3, 100, -2} sonucunu verir.
#bu değerler kume1 de olup kume2 de olmayan değerlerdir.

print(kume2.difference(kume1))
#{-1, 23} sonucunu verir.
#bu değerler kume2 de olup kume1 de olmayan değerlerdir.

#Bu metot sadece iki kümenin birbirlerine göre farkını gösterir.
#Kümelerin değerlerinde herhangi bir farklılık olmaz.


#difference_update(): Birinci kümenin ikinci kümeden farkını döndürüp, 
#o farkı birinci kümeye atarak birinci kümeyi günceller.
#yani birinci kümenin elemanlarının hepsi artık ikinci kümeyle olan farkı olur.

kume1.difference_update(kume2)
print(kume1)

#discard(): Kümeden eleman çıkartmak için kullanılır.
#eğer kümede öyle bir eleman yoksa, hata vermez. Hiç bir işlem yapmaz.

#intersection(): Kümelerin kesişim elemanlarını döndürür.

#intersection_update(): Kümelerin kesişimini alıp birinci kümeye atama işlemini yapar.

kume1= {1,2,3,10,34,100,-2}
kume2= {1,2,23,34,-1}

kume1.intersection_update(kume2)
print(kume1)
#{1, 2, 34} sonucunu verir.

#isdisjoint(): İki kümenin ayrık küme olup olmadığına bakar.
#yani kesişim kümeleri boşsa ayrık kümelerdir.
#Eğer ayrık kümelerse true, değillerse false döner.

kume1= {1,2,3,10,34,100,-2}
kume2= {1,2,23,34,-1}
kume3= {30,40,50}

print(kume1.isdisjoint(kume2))
#False döner çünkü bu ikisinin ortak elemanları var. Yani ayrık küme değiller.

print(kume1.isdisjoint(kume3))
#True döner çünkü ortak elemanları yok. Yani ayrık kümeler.


#issubset(): Bu metot, birinci küme ikinci kümenin alt kümesiyse true, değilse false döner.

kume1= {1,2,3}
kume2= {1,2,3,4}
kume3= {5,6,7}

print(kume1.issubset(kume2))
#True döner

print(kume1.issubset(kume3))
#False döner.


#union(): Bu metot, iki kümenin birleşim kümesini döndürür.

#update(): İkinci kümeyi birinci kümeye atar. Yani aslında iki kümenin birleşim kümesini birinci kümeye aktarır.

