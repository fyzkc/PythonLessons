#sınıflar içerisine metotlar eklemek normal fonksiyon tanımlamakla aynıdır.

#bir sınıf içerisinde ürettiğimiz metotlar, o sınıftan ürettiğimiz nesnelere özgü olur ve 
#o nesneler üzerinde bu metotları kullanabiliriz.

class Yazilimci():
    def __init__(self,isim,soyIsim,numara,maas,diller):
        self.isim=isim
        self.soyIsim = soyIsim
        self.numara = int(numara)
        self.maas= int(maas)       
        self.diller = diller

#NOT: Metot tanımlamanın normal fonksiyon tanımlamaktan tek farkı mutlaka self parametresini
#içermesi gerekir. Çünkü herhangi bir özelliğe erişmek için self referansını göndermemiz gerekir.

    def BilgileriGoster(self):
        print("""
        Yazılımcı nesnesinin özellikleri
        İsim: {}
        Soyisim: {}
        Numara: {}
        Maaş: {}
        Bildiği Diller: {}

        """.format(self.isim,self.soyIsim,self.numara,self.maas,self.diller)
        )

    def ZamYap(self,zamMiktari):
        print("Zam Yapılıyor.")
        self.maas += zamMiktari
        print("Yeni maaşınız: {}".format(self.maas))

    def DilEkle(self,yeniDil):
        print("Dil Ekleniyor")
        self.diller.append(yeniDil)
        print("Yeni dil eklendi.")


yazilimci1 = Yazilimci("Feyza","Koç","12345","10000",["Python","C#","C"])

yazilimci1.BilgileriGoster()
yazilimci1.ZamYap(2000)
yazilimci1.DilEkle("Java")
yazilimci1.BilgileriGoster()



