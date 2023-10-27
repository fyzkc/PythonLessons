"""
Super anahtar kelimesi, miras aldığımız sınıfın metotlarını alt sınıflarda kullanabilmemizi sağlar.

"""

class Calisan():
    def __init__(self,isim,maas,departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim=isim
        self.maas=int(maas)
        self.departman=departman

    def BilgileriGoster(self):
        print("Çalışan sınıfının bilgileri: ")
        print("İsim: {}\nMaaş: {}\nDepartman: {}".format(self.isim,self.maas,self.departman))

    def DepartmanDegistir(self,yeniDepartman):
        self.departman= yeniDepartman

class Yonetici(Calisan):
    def __init__(self, isim, maas, departman,kisiSayisi):
        print("Yönetici sınıfının init fonksiyonu")
        self.isim=isim
        self.maas=int(maas)
        self.departman=departman
        self.kisiSayisi = int(kisiSayisi)
    def zamYap(self,zamMiktari):
        self.maas+= zamMiktari

#Super anahtar kelimesinin kullanılmasının sebebi şudur:
"""
Diyelim ki biz init fonksiyonunnu Yonetici sınıfında override etmek istiyoruz. Ancak Calisan sınıfındaki init fonksiyonu içerisindeki
self.isim=isim
self.maas=int(maas)
self.departman=departman
alanlarını tekrar kullanıp, yalnızca ekstra bir özellik eklemek istiyoruz.
O zaman bu üç özelliği tekrar yazmakla uğraşmak yerine super anahtar kelimesini kullanabiliriz.

"""
class Yonetici(Calisan):
    def __init__(self, isim, maas, departman,kisiSayisi):
        super().__init__(isim,maas,departman)
        print("Yönetici sınıfının init fonksiyonu")
        self.kisiSayisi = int(kisiSayisi)
    def zamYap(self,zamMiktari):
        self.maas+= zamMiktari

#burada super ile calisan sınıfındaki isim, maas ve departman özelliklerini yönetici sınıfında da kullanacağımızı belirtmiş olduk.

yonetici2= Yonetici("Feyza",30000,"IT",5)

"""
bu şekilde biz yönetici sınıfından bir nesne tanımladığımızda önce miras aldığı çalışan fonksiyonunun init fonksiyonu,
daha sonra da kendi sınıfının init fonksiyonu çalışır. Ekran çıktısı şu şekilde olur:

Çalışan sınıfının init fonksiyonu
Yönetici sınıfının init fonksiyonu

"""

