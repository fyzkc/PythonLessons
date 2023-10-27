"""Bir şirket programı düşünelim.
Program içerisindeki sınıflar: Çalışanlar
Bu programdaki özellikler ve metotlar şu şekilde olsun:
Çalışanlar sınıfı özellikleri: Çalışanların adı, soyadı, numarası, departmanı, maaşı
Çalışanlar sınıfı metotları: çalışan bilgilerini gösterme, çalışanın maaşını arttırma, çalışanın departmanını değiştirme
emekliliğine kaç yıl kaldığını göster
"""

import datetime

class Calisanlar():
    def __init__(self,calisanAd,calisanSoyad,calisanDogum,calisanNumara,calisanDepartman,calisanMaas,calisanEmeklilik):
        self.calisanAd = calisanAd
        self.calisanSoyad = calisanSoyad
        self.calisanDogumTarihi = int(calisanDogum)
        self.calisanNumara = int(calisanNumara)
        self.calisanDepartman = calisanDepartman
        self.calisanMaas = int(calisanMaas)
        self.calisanEmeklilik = int(calisanEmeklilik)
        tarih = datetime.datetime.now()
        self.yil= tarih.year

    def BilgileriGoster(self):
        print("""
        Çalışanın bilgileri:
              İsim: {}
              Soyisim: {}
              Doğum Tarihi: {}
              Numara: {}
              Departman: {}
              Maaş: {}
              Emeklilik Yılı: {}
        """.format(self.calisanAd,self.calisanSoyad,self.calisanDogumTarihi,self.calisanNumara,self.calisanDepartman,self.calisanMaas,self.calisanEmeklilik))

    def MaasArttir(self,zamMiktari):
        self.calisanMaas += zamMiktari
        print("Çalışanın yeni maaş miktarı: {}".format(self.calisanMaas))
    
    def DepartmanDegistir(self,yeniDepartman):
        self.calisanDepartman = yeniDepartman
        print("Çalışanın yeni departmanı: {}".format(self.calisanDepartman))

    def EmeklilikKalanYil(self):
        print(self.calisanEmeklilik-self.yil)


calisan1= Calisanlar("Feyza","Koç",2001,1234567890,"IT",25000,2056)

calisan1.BilgileriGoster()
calisan1.EmeklilikKalanYil()

calisan1.MaasArttir(2500)
calisan1.DepartmanDegistir("Pazarlama")

calisan1.BilgileriGoster()