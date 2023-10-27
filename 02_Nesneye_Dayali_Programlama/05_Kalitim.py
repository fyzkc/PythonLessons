"""
Kalıtım bir sınıfın başka bir sınıfın özelliklerini ve metotlarını miras almasıdır.
Bir sınıf başka bir sınıftan miras aldığında, miras aldığı sınıfın özelliklerini ve metotlarını alır.
Bu nerede işe yarar?

Diyelim ki bir şirketin çalışanlarını sınıf olarak tasarlamak istiyoruz. Bunun için yönetici, proje direktörü vs gibi sınıflar üretmemiz gerekiyor.
Ancak bu sınıfların hepsinin ortak özellikleri ve metotları olabilir (çalışanın adı, soyadı vs gibi).
Biz bu ortak olan özellikleri ve metotları tekrar tekrar tanımlamak yerine kalıtım özelliğinden faydalanabiliriz.

"""

class Calisan():
    #çalışan sınıfı bizim ana sınıfımız olacak ve bundan sonra üreteceğimiz sınıflar bu sınıftan miras alacak.
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
    #Yönetici sınıfı Çalışan sınıfından miras almış oldu.
    pass #Bu ifade blok içerisine sonradan tanımlama yapmak istiyorsak, hata almamak için boşluk bırakmamak adına kullanılır.

#Yönetici sınıfına Çalışan sınıfından miras aldırdığımız için, Çalışan sınıfı içerisindeki init fonksiyonu
#bilgilerigoster fonksiyonu ve departmandegistir fonksiyonu olduğu gibi Yönetici sınıfına da geçmiş oldu.

yonetici1= Yonetici("Feyza Koç",10000,"IT")

#Bu kodu çalıştırdığımız zaman "Çalışan sınıfının init fonksiyonu" yazısını görürüz.
#Bunun anlamı, yönetici sınıfı çalışan sınıfından miras aldığı için ve init fonksiyonu da bir nesne türetildiğinde
#ilk çağırılan fonksiyon olduğu için, yönetici sınıfından bir nesne türettiğimizde çalışan sınıfının init fonksiyonu içerisine
#yazdığımız şeyi ekranda gördük.

yonetici1.BilgileriGoster()

yonetici1.DepartmanDegistir("İnsan Kaynakları")
yonetici1.BilgileriGoster()


#Bu şekilde yönetici sınıfı çalışan sınıfından miras almış olur. Ancak biz bu yönetici sınıfına ekstra
#özellikler ve metotlar da ekleyebiliriz.

class Yonetici(Calisan):
     #Yönetici sınıfımızı yeniden tanımlayalım
     def zamYap(self,zamMiktari):
         self.maas+= zamMiktari


yonetici2= Yonetici("Merve Koç",20000,"Kimya")

yonetici2.zamYap(500)

yonetici2.BilgileriGoster()
