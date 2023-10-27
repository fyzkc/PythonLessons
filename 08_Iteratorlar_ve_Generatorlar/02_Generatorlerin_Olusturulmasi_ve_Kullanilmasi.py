"""
Generatorler, Python'da iterable objeler oluşturmak için kullanılan
objelerdir ve bellekte herhangi bir yer kaplamazlar.

Örneğin, 100.000 tane değer üretip bu değerleri bir listede tutmak isgtersek
bellekte oldukça fazla yer kaplayacaktır. O yüzden bu işlemi gerçekleştiren bir fonksiyonu
generator olarak yazmak çok daha verimli olmasını sağlar.

"""

def kareleriAl():
    sonuc= []
    for i in range(1,6):
        sonuc.append(i**2)
    return sonuc

print(kareleriAl())

#Bu işlemde yalnızca 5 tane sayının karesini alıp ekrana yazdırdık.
#Ancak çok daha fazla sayının karelerini yazdırmak istersek,
#Bu sayıları bir listede saklamak çok fazla yer kaplamasına sebep olacaktır.

def kareleriAl2():
    for i in range(1,6):
        yield i**2

#Generator oluşturmak için yield anahtar kelimesini kullanıyoruz.

gerenator = kareleriAl2()

#Önceki fonksiyonumuzda bir her bir sayının karesini sırayla bir listede tutuyorduk
#Bu yüzden değerlere direkt olarak erişebilyorduk.
#Ancak generator içerisindeki yield anahtar sözcüğünün anlamı şudur:
#Aslında bu değerler, henüz üretilmedi. Yani sayıların kareleri henüz üretilmedi ve bir yerde saklanmadı.
#Bu değerler sadece, erişildiğinde üretilecek.
#Ancak bunlara print() metoduyla erişemeyiz.

#generator objesi iterable bir obje olduğundan bu objeden bir iterator oluşturalım.

iterator=iter(gerenator)

#Eğer generator objemizden br-ir elemana erişmek istemezsek,
#generator içerisinde bulunan yield anahtar kelimesinin olduğu 
#ilk satırdan itibaren, kod durur.
#Yani eğer herhangi bir elemana erişmek istemezsek, yield anahtar kelimesinden
#sonra kısım çalışmıyor.
#Sadece bir elemana erişmek istersek o değeri üretiyor.
#Bunun sebebi ise, değerleri önceden ürettiği zaman bir bellek alanında
#yer tutması gerekir. Ancak bu şekilde, sadece erişeleceği zaman üretip,
#değerlerin bellekte yer tutmasının önüne geçilmiş oluyor.

print(next(iterator))
#Bunu yaptığımız zaman ekranda ilk sayının karesini ekrana verir.
print(next(iterator))
#4 sayısı ekrana yazılır.

#Bu değerler üretildikten ve gösterildikten sonra, daha önce de dediğim gibi,
#hafızada yer kaplamadığı için, üretilir, gösterilir ve yok olur.
#Bu değerleri bir değişkende tutmamız mümkün değildir.


#Peki bir list comprehension'ı nasıl generatora çevirebiliriz?

liste= [i*3 for i in range(5)]
#bu bir list comprehension'dır.
generator=(i*3 for i in range(5))
#bu ise generator halidir.
#yani [] yerine () koymamız yeterli olur.

iterator=iter((i*3 for i in range(5)))
print(next(iterator)) #0
print(next(iterator)) #3
print(next(iterator)) #6

def carpimTablosu():
    for i in range(1,11):
        for j in range(1,11):
            yield "{} * {} = {}".format(i,j,i*j)

for i in carpimTablosu():
    print(i)

"""
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
1 * 7 = 7
1 * 8 = 8
1 * 9 = 9
1 * 10 = 10
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27
3 * 10 = 30
4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
4 * 4 = 16
4 * 5 = 20
4 * 6 = 24
4 * 7 = 28
4 * 8 = 32
4 * 9 = 36
4 * 10 = 40
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
6 * 6 = 36
6 * 7 = 42
6 * 8 = 48
6 * 9 = 54
6 * 10 = 60
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
7 * 7 = 49
7 * 8 = 56
7 * 9 = 63
7 * 10 = 70
8 * 1 = 8
8 * 2 = 16
8 * 3 = 24
8 * 4 = 32
8 * 5 = 40
8 * 6 = 48
8 * 7 = 56
8 * 8 = 64
8 * 9 = 72
8 * 10 = 80
9 * 1 = 9
9 * 2 = 18
9 * 3 = 27
9 * 4 = 36
9 * 5 = 45
9 * 6 = 54
9 * 7 = 63
9 * 8 = 72
9 * 9 = 81
9 * 10 = 90
10 * 1 = 10
10 * 2 = 20
10 * 3 = 30
10 * 4 = 40
10 * 5 = 50
10 * 6 = 60
10 * 7 = 70
10 * 8 = 80
10 * 9 = 90
10 * 10 = 100
"""

#range() fonksiyonu generatorlar ile yazılmış bir fonksiyondur.
#yani biz range(100000) dediğimiz zaman 0'dan 100000'e kadar olan sayıları
#bellekte herhangi bir yerde saklamaz. Sadece o değeri üretiyor ve kullanıyoruz.
