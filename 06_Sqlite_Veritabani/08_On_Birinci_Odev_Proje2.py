"""
Proje 2
Süpermarket içindeki ürünler üzerinden bir tane Süpermarket Projesi geliştirmeye çalışın.

"""
import sqlite3
import time
from os import system

class Urun():
    def __init__(self,urunAd,bolum,stokDurumu,fiyat):
        self.urunAd=urunAd
        self.bolum=bolum
        self.stokDurumu=stokDurumu
        self.fiyat=fiyat

    def __str__(self):
        return "Ürün Bilgileri:\nÜrün: {}\nÜrünün Bulunduğu Bölüm: {}\nStok Durumu: {}\nFiyat: {}\n".format(self.urunAd,self.bolum,self.stokDurumu,self.fiyat)
    

class SuperMarket():
    def __init__(self):
        self.BaglantiOlustur()

    def BaglantiOlustur(self):
        self.baglanti= sqlite3.connect("Supermarket.db")
        self.cursor= self.baglanti.cursor()

        sorgu = "CREATE TABLE IF NOT EXISTS TumUrunler (Urun TEXT, Bolum TEXT, StokDurumu INT, Fiyat INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def UrunleriGoster(self):
        sorgu= "SELECT * FROM TumUrunler"
        self.cursor.execute(sorgu)
        urunler= self.cursor.fetchall()

        if(len(urunler)==0):
            print("Hiç ürün yok.")
        else:
            for i in urunler:
                urun = Urun(i[0],i[1],i[2],i[3])
                print(urun)

    def ReyondakiUrunleriGoster(self,reyonad):
        sorgu = "SELECT * FROM TumUrunler WHERE Bolum = ?"
        self.cursor.execute(sorgu,(reyonad,))
        urunler= self.cursor.fetchall()
        if(len(urunler)==0):
            print("Bu reyonda hiç ürün yok.")
        else:
            for i in urunler:
                urun = Urun(i[0],i[1],i[2],i[3])
                print(urun)


    def UrunEkle(self,urunBilgi):
        sorgu = "INSERT INTO TumUrunler VALUES (?,?,?,?)"
        self.cursor.execute(sorgu,(urunBilgi.urunAd,urunBilgi.bolum,urunBilgi.stokDurumu,urunBilgi.fiyat))
        self.baglanti.commit()

    def UrunSil(self,urunad):
        urunKontrol= "SELECT * FROM TumUrunler WHERE Urun = ?"
        self.cursor.execute(urunKontrol,(urunad,))
        varMi= self.cursor.fetchall()
        if(len(varMi)==0):
            print("Böyle bir ürün zaten yok.")
        else:
            sorgu = "DELETE FROM TumUrunler WHERE Urun = ?"
            self.cursor.execute(sorgu,(urunad,))
            self.baglanti.commit()

    def StokDurumuGoruntule(self,urunad):
        sorgu = "SELECT * FROM TumUrunler WHERE Urun = ?"
        self.cursor.execute(sorgu,(urunad,))
        urunVarmi= self.cursor.fetchall()
        if(len(urunVarmi)==0):
            print("Böyle bir ürün stoklarımızda yok.")
        else:
            sorgu2 = "SELECT StokDurumu FROM TumUrunler WHERE Urun = ?"
            self.cursor.execute(sorgu2,(urunad,))
            stok= self.cursor.fetchall()
            print(stok)

    def StokArttir(self,urunad):
        sorgu = "SELECT * FROM TumUrunler WHERE Urun = ?"
        self.cursor.execute(sorgu,(urunad,))
        urunAdi= self.cursor.fetchall()
        if(len(urunAdi)==0):
            print("Böyle bir ürün stoklarımızda yok.")
            return False
        else:
            stokSayisi= urunAdi[0][2]
            stokSayisi +=1
            sorgu= "UPDATE TumUrunler SET StokDurumu = ? WHERE Urun = ?"
            self.cursor.execute(sorgu,(stokSayisi,urunad))
            self.baglanti.commit()

    
    def StokAzalt(self,urunad):
        sorgu = "SELECT * FROM TumUrunler WHERE Urun = ?"
        self.cursor.execute(sorgu,(urunad,))
        urunAdi= self.cursor.fetchall()
        if(len(urunAdi)==0):
            print("Böyle bir ürün stoklarımızda yok.")
            return False
        else:
            stokSayisi= urunAdi[0][2]
            stokSayisi -=1
            sorgu= "UPDATE TumUrunler SET StokDurumu = ? WHERE Urun = ?"
            self.cursor.execute(sorgu,(stokSayisi,urunad))
            self.baglanti.commit()
            sorgu2 = "SELECT StokDurumu FROM TumUrunler WHERE Urun = ?"
            self.cursor.execute(sorgu2,(urunad,))
            stokvarmi = self.cursor.fetchall()
            if(stokvarmi == [(None,)]):
                sorgu3 = "DELETE FROM TumUrunler WHERE Urun = ?"
                self.cursor.execute(sorgu3,(urunad,))
                self.baglanti.commit()




market = SuperMarket()

while(True):
    print("""

    SüperMarket Programına Hoşgeldiniz!
          İşlemler:
          1. Bütün Ürünleri Görüntüleme
          2. Reyondaki Ürünleri Görüntüleme
          3. Ürün Ekleme
          4. Ürün Silme
          5. Ürünün Stok Durumunu Görüntüleme
          6. Stok Arttırma
          7. Stok Azaltma

    Çıkmak için 'q' ya basın.

""")
    giris= input("\nYapmak istediğiniz işlemi girin: \n")
    if(giris=='q'):
        print("Programdan çıkılıyor...")
        time.sleep(1)
        break
    elif(giris == '1'):
        time.sleep(1)
        system("cls")
        market.UrunleriGoster()
        time.sleep(1)
    elif(giris == '2'):
        reyonad = input("Görüntülemek istediğiniz reyonu yazın:\nŞarküteri\nManav\nTemizlik\nAtıştırmalıklar\nUnlu Mamüller\nKozmetik\nReyon ismini doğru yazdığınızdan emin olun!\n")
        time.sleep(1)
        system("cls")
        market.ReyondakiUrunleriGoster(reyonad)
        time.sleep(1)
    elif(giris == '3'):
        urunadi = input("Ürün: ")
        reyon = input("Ürünün reyonu: ")
        stok = int(input("Stok: "))
        fiyat = int(input("Fiyat: "))
        print("Ürün ekleniyor, lütfen bekleniyiniz..")
        time.sleep(1)
        urun= Urun(urunadi,reyon,stok,fiyat)
        time.sleep(1)
        system("cls")
        market.UrunEkle(urun)
        print("Ürün başarılı bir şekilde eklendi.")
        time.sleep(1)
    elif(giris == '4'):
        giris= input("Silmek istediğiniz ürünün adını yazınız: ")
        eminmisin= input("Bu ürünü silmek istediğinizden emin misiniz? Bu işlem geri alınamaz! (E/H)?")
        if(eminmisin=='E'):
            print("Ürün silinirken lütfen bekleyiniz.")
            time.sleep(1)
            system("cls")
            market.UrunSil(giris)
            print("Ürün silindi.")
            time.sleep(1)
    elif(giris == '5'):
        giris= input("Stok durumunu görüntülemek istediğiniz ürünün adını yazınız: ")
        time.sleep(1)
        system("cls")
        market.StokDurumuGoruntule(giris)
    elif(giris == '6'):
        giris= input("Stoğunu arttırmak istediğiniz ürünün adını yazınız: ")
        print("Lütfen bekleyiniz..")
        time.sleep(1)
        if(market.StokArttir(giris)!=False):
            time.sleep(1)
            system("cls")
            market.StokArttir(giris)
            print("Stok güncellendi.")
            time.sleep(1)
    elif(giris == '7'):
        giris= input("Stoğunu azaltmak istediğiniz ürünün adını yazınız: ")
        print("Lütfen bekleyiniz..")
        time.sleep(1)
        if(market.StokAzalt(giris)!=False):
            time.sleep(1)
            system("cls")
            market.StokAzalt(giris)
            print("Stok güncellendi.")
            time.sleep(1)



