"""
Generator bir fibonacci serisi yapalım.
"""

def fibonacci():
    a=1
    b=1
    #öncelikle bu a ve b değerlerini üretelim.
    yield a 
    yield b
    while(True):
        a,b = b, a+b
        #bu kodun anlamı, b değerini a'ya,
        #a+b değerini de b'ye atıyoruz.
        yield b
        #b değeri a+b olacağı için b değerini üretmek için yield b diyoruz.

for i in fibonacci():
    if(i>100000):
        break
    else:
        print(i)

"""
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765
10946
17711
28657
46368
75025
"""

#Öncelikle ilk a ve b değerleri olan 1 sayılarını ekranda görebilmek için
#yield kelimesi ile a ve b değerlerini ürettik.

#Daha sonra b değerini a'ya atadık.
#a+b değerini de b ye atadık.
#burada a'nın yeni değeri 1,
#b'nin yeni değeri de 2 oldu.

#toplanan ifade fibonacci serisinin bir sonraki elemanı olacağından,
#b sayısını ekrana yazdırabilmek için yield b dedik.

#yani aslında yield kelimesi kullanarak değeri üretmek demek,
#o değeri  kullanıma açmak demek.
#biz for döngüsü ile o değerleri ekrana bastıracağımzdan,
#o değerlerim üretilmesi gerekecek.
#üretilen değerleri böylece istediğimiz işlem için kullanabileceğiz.
#bizim burda kullandığımız işlem ise ekrana bastırmak.
#yani özetle yield kelimesi değerin kullanıma hazır hale getirilmesi anlamına geliyor.

