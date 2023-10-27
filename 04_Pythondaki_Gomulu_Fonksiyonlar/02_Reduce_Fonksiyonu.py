#reduce() fonksiyonunun yapısı:

# reduce(fonksiyon,(liste,demet,vb.))

#yapısı map fonksiyonuna benzeyen bu fonksiyon, verilen liste üzerinde
#soldan başlayarak sırasıyla tüm elemanlara gönderilen fonksiyonu uygular.
#önce ilk iki elemana uygular ve sonrasında sırayla diğer elemanlarla devam eder.

from functools import reduce
#reduce fonksiyonu functools modülüne taşınmıştır.

sonuc= reduce(lambda x,y : x+y , [12,18,20,10])
print(sonuc)

#fonksiyonumuz, gönderilen iki değeri topluyor.
#reduce fonksiyonuna gönderildiğinde, öncelikle 12 ile 18 sayılarını toplar.
#Daha sonra çıkan sonuca 20 sayısını ekler ve sonra yine aynı şekilde çıkan sonuca 10 sayısını ekler.
#Ve sonuç 60 bulunmuş olur.

#reduce fonksiyonu kümülatif bir fonksiyondur.

#reduce fonksiyonu kullanarak faktöriyel hesabı:

fak=reduce(lambda x,y: x*y,[1,2,3,4,5])
print(fak)

#Bu şekilde uzun faktöriyel hesapları reduce fonksiyonu kullanarak yapılabilir.

#Bir dizi içerisindeki en büyük sayısını bulma:

def maks(x,y):
    if(x>y):
        return x
    else:
        return y

maksimum= reduce(maks,[-2,3,1,4])
print(maksimum)
