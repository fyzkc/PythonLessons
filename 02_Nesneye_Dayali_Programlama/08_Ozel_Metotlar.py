"""
Özel metotlar, bizim özel olarak çağırmadığımız ama her sınıfa ait metotlardır.
Bunların çoğu python tarafından varsayılan olarak tanımlanır. Ancak özel olarak kendimiz de her bir metotu yeniden tanımlayabiliriz.
Örneğin init fonksiyonu.

"""

class Kitap():
    pass

#Kitap isimli bir class oluşturduk.

kitap = Kitap()
#biz bu nesneyi ürettiğimizde python varsayılan olan init metodunu çağırır.
#print(kitap)
#bu kod sonucu da python tarafından varsayılan olan __str__ metodunu çağırır.
del kitap
#bu kod da yine varsayılan olarak tanımlanan __del__ metodunu çağırır. Bu metot yanına yazılan nesnenin silinmesini sağlar.

#Şimdi bu metotları kendimiz tanımlayalım.

class Kitap():
    def __init__(self,isim,yazar,sayfaSayisi,tur):
        print("Kitap classının init fonksiyonu")
        self.isim= isim
        self.yazar=yazar
        self.sayfaSayisi=sayfaSayisi
        self.tur=tur
    def __str__(self):
        return "İsim: {}\nYazar: {}\nSayfa Sayısı: {}\nTürü: {}".format(self.isim,self.yazar,self.sayfaSayisi,self.tur)
    


kitap1=Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye")
#bu nesne tanımlandıktan sonra "Kitap classının init fonksiyonu" yazısı ekranda görülür.
print(kitap1)
""" bu kod da bize 

İsim: İstanbul Hatırası
Yazar: Ahmet Ümit
Sayfa Sayısı: 561
Türü: Polisiye

sonucunu döndürecektir.
"""

# NOT: __del__ metodu override edilemez, sadece üzerine ekstra özellik eklenebilir.


