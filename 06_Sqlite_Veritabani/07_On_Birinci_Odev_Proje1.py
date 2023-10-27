"""
Proje 1
Siz de bir tane Şarkı projesi geliştirmeye çalışın.

                     Örnek özellikler;

                     1. Şarkı İsmi 
                     2. Sanatçı
                     3. Albüm
                     4. Prodüksiyon Şirketi
                     5. Şarkı Süresi

                     Örnek Metodlar;

                     1. Veritabanındaki Toplam Şarkı Süresini Hesaplayan Metod
                     2. Şarkı Ekle
                     3. Şarkı Sil

                     Benim ekstra olarak yapmak istediğim fonksiyonlar:
                     1. Şarkıları Göster
                     2. Sanatçıları Göster
"""

import sqlite3
import time

class Sarki():
    def __init__(self,isim,sanatci,album,produksiyonSirketi,sure):
        self.isim=isim
        self.sanatci=sanatci
        self.album=album
        self.produksiyonSirketi=produksiyonSirketi
        self.sure=sure

    def __str__(self):
        return "Şarkı: {}\nSanatçı: {}\nAlbüm: {}\nProdüksiyon Şirketi: {}\nŞarkı Süresi: {}\n".format(self.isim,self.sanatci,self.album,self.produksiyonSirketi,self.sure)
    

class CalmaListesi():
    def __init__(self):
        self.CalmaListesiOlustur()

    def CalmaListesiOlustur(self):
        self.baglanti= sqlite3.connect("ÇalmaListesi.db")

        self.cursor=self.baglanti.cursor()

        sorgu = "CREATE TABLE IF NOT EXISTS Sarkilar (Şarkı TEXT, Sanatçı TEXT, Albüm TEXT, Prodüksiyon_Şirketi TEXT, Şarkı_Süresi INT)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()

    def BaglantiKapat(self):
        self.baglanti.close()

    def SarkilariGoruntule(self):
        goruntule= "SELECT * FROM Sarkilar"
        self.cursor.execute(goruntule)
        sarkilar = self.cursor.fetchall() #Tüm şarkıları getir sorgusunu çalıştırdıktan sonra tüm veriyi sarkilar değişkenine atalım.

        if(len(sarkilar)==0):
            print("Bu çalma listesinde hiç şarkı yok.")
        else:
            for i in sarkilar: #i, burada bütün veri içerisindeki her bir satır oluyor.
                sarki=Sarki(i[0],i[1],i[2],i[3],i[4]) #birinci satırın 0. elemanı şarkının ismi, 1. elemanı şarkının sanatçısı vs diye tüm değerleri vererek ekranda görüntüleyebilmek adına bir sarki nesnesi oluşturuyoruz.
                print(sarki) #tanımladığımız str metodu sayesinde print ile şarkının bilgilerini ekrana kolaylıkla yazdırabiliyoruz.

    def SanatcilariGoster(self):
        sorgu = "SELECT Sanatçı FROM Sarkilar"
        self.cursor.execute(sorgu)
        sanatcilar = self.cursor.fetchall()

        if(len(sanatcilar)==0):
            print("Çalma listesindeki hiç bir şarkının sanatçı bilgisi bulunmuyor.")
        else:
            for i in sanatcilar:
                print(i)

    def ToplamSarkiSuresi(self):
        sorgu= "SELECT SUM(Şarkı_Süresi) AS Toplam_Şarkı_Süresi FROM Sarkilar"
        self.cursor.execute(sorgu)
        toplamSure= self.cursor.fetchall()
        if(toplamSure == [(None,)]):
            return False
        else:
            print(toplamSure)

    def SarkiEkle(self,sarki):
        ekle= "INSERT INTO Sarkilar VALUES (?,?,?,?,?)"
        self.cursor.execute(ekle,(sarki.isim,sarki.sanatci,sarki.album,sarki.produksiyonSirketi,sarki.sure))
        self.baglanti.commit()

    def SarkiSil(self,isim):
        sorgu = "SELECT * FROM Sarkilar WHERE Şarkı = ?"
        self.cursor.execute(sorgu,(isim,))
        sarki= self.cursor.fetchall()

        if(len(sarki)==0):
            print("Böyle bir şarkı zaten bulunmamakta.")
        else:
            sil= "DELETE FROM Sarkilar WHERE Şarkı = ?"
            self.cursor.execute(sil,(isim,))
            self.baglanti.commit()


print("""

Çalma Listesi Programına Hoşgeldiniz!

      İşlemler:

      1. Şarkıları Görüntüle
      2. Sanatçıları Görüntüle
      3. Çalma Listesindeki Şarkıların Toplam Süresini Görüntüleme
      4. Şarkı Ekleme
      5. Şarkı Silme

Programdan çıkmak için 'q' ya basın.

""")

calmalistesi= CalmaListesi()
while(True):
    giris= input("Yapmak istediğiniz işlemi girin: ")
    if(giris=='q'):
        print("Programdan çıkılıyor..")
        time.sleep(1)
        break
    elif(giris=='1'):
        calmalistesi.SarkilariGoruntule()
    elif(giris=='2'):
        calmalistesi.SanatcilariGoster()
    elif(giris=='3'):
        if(calmalistesi.ToplamSarkiSuresi()==False):
            print("Bu listede hiç şarkı yok")
        else:
            print("***")
            calmalistesi.ToplamSarkiSuresi()
            print("***")
    elif(giris=='4'):
        isim= input("Şarkı: ")
        sanatci= input("Sanatçı: ")
        album = input("Albüm: ")
        produksiyon = input("Prodüksiyon Şirketi: ")
        sure = int(input("Şarkının Süresi :"))
        sarki= Sarki(isim,sanatci,album,produksiyon,sure)
        print("Şarkı ekleniyor...")
        time.sleep(1)
        calmalistesi.SarkiEkle(sarki)
        print("Şarkı başarıyla eklendi.")
    elif(giris=='5'):
        isim= input("Silmek istediğiniz şarkı: ")
        cevap = input("Bu şarkıyı silmek istediğinizden emin misiniz? Bu işlem geri alınamaz! (E/H)")

        if(cevap=='E'):
            print("Şarkı siliniyor..")
            time.sleep(1)
            calmalistesi.SarkiSil(isim)
            print("Şarkı silindi.")
        