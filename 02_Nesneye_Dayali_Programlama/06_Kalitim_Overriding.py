"""
Overriding:
Bir sınıftan miras alan diğer sınıflar, miras aldığı sınıf içerisindeki özellikleri
ve metotları kullanır. Ancak miras aldığı sınıftaki metotlardan birini, miras alan sınıf kendi içinde
yine aynı isimle yeniden tanımlarsa, miras aldığı sınıftaki metotun üzerine yazmış olur (override).
Ve bu şekilde miras alan sınıfta bu metotu çağırdığımızda, miras aldığı sınıftaki değil kendi sınıfında tanımladığı aynı isimli metot çalışır.

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
      

#Yönetici sınıfından bir obje türetelim.

yonetici1 = Yonetici("feyza koç",30000,"IT",5)

#bu kod çalıştığında ekran çıktısı "Yönetici sınıfının init fonksiyonu" olur.


calisan1= Calisan("Feyza Koç",20000,"IT")

#bu kod çalıştığında ekran çıktısı "Çalışan sınıfının init fonksiyonu" olur.

#Yine aynı şekilde başka metotları da override edebiliriz.

# NOT: Bir metodu override edebilmek için, metotun önceki halinden farklı olması lazım. Metot ismi aynı olduğu için
#aldığı parametreleri farklı olmalı.


