"""
Problem 1
Elinizde bir dikdörtgenin kenarlarını ifade eden sayı çiftlerinin bulunduğu bir liste olsun.

         [(3,4),(10,3),(5,6),(1,9)]

Şimdi kenar uzunluklarına göre dikdörtgenin alanını hesaplayan bir fonksiyon yazın ve 
bu listenin her bir elemanına bu fonksiyonu uygulayarak ekrana şöyle bir liste yazdırın.

         [12, 30, 30, 9]

*Not : map() fonksiyonunu kullanmaya çalışın.*
"""

def alanBul(x,y):
    return x*y

birinciKenar=list()
ikinciKenar=list()

liste=[(3,4),(10,3),(5,6),(1,9)]

for i in liste:
    birinciKenar.append(i[0])
    ikinciKenar.append(i[1])


alanlar=(list(map(alanBul,birinciKenar,ikinciKenar)))
print(alanlar)

#------------------------------------------------------------

#  ÇÖZÜM :

#------------------------------------------------------------

print("------------------------------------------------")

def alan_hesapla(demet):
    return demet[0] * demet[1]

liste = [(3,4),(10,3),(5,6),(1,9)]

print(list(map(alan_hesapla,liste)))

#Çözümün açıklaması:

#map fonksiyonuna parametre olarak verilen fonksiyona, diğer parametre olan listenin her bir elemanı tek tek gider.
#Yani fonksiyon listenin her elemanına tek tek işlem yapar.
#Burada listenin ilk elemanı (3,4) demetidir.
#İkinci elemanı (10,3),
#Üçüncü elemanı (5,6) ve
#Son elemanı da (1,9) dur.
#map fonksiyonu içerisine verilen alan_hesapla fonksiyonuna sırasıyla bu elemanlar tek tek gönderilir.
#İlk gönderilen eleman (3,4) demetidir.
#Ve bu demet üzerinden demetin 0. elemanı ile 1. elemanı çarpılır ve çarpım sonucu döndürülür.
#Aynı şekilde diğer elemanlar da tek tek gönderilerek kendi içlerinde çarpılır ve sonuç bir liste olarak döndürülür.
