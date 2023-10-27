import random
import time

class Kumanda():
    def __init__(self,tvDurum = "Kapalı",tvSes=0,kanalListesi=["TRT"],acikKanal="TRT"):
        self.tvDurum=tvDurum
        self.tvSes=tvSes
        self.kanalListesi= kanalListesi
        self.acikKanal=acikKanal
    
    def tvAc(self):
        if(self.tvDurum=="Kapalı"):
            print("Televizyon açılıyor.")
            self.tvDurum="Açık"
    def tvKapat(self):
        if(self.tvDurum=="Açık"):
            print("Televizyon kapatılıyor.")
    def sesAyarla(self):
        while(True):
            cevap= input("Sesi azalt: '<' \nSesi Arttır: '>'")
            if(cevap=="<"):
                if(self.tvSes!=0):
                    self.tvSes-=1
                    print("Ses: ",self.tvSes)
            elif(cevap==">"):
                if(self.tvSes!=50):
                    self.tvSes+=1
                    print("Ses: ",self.tvSes)
            else:
                print("Ses: ",self.tvSes)
                print("Ses ayarından çıkılıyor.")
                break
    
    def kanalEkle(self,kanalIsim):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanalListesi.append(kanalIsim)
        print("Kanal Eklendi")

    def kanalDegistir(self):
        while(True):
            cevap= input("Bir önceki kanal: '<'\nBir sonraki kanal: '>'")
            indis= self.kanalListesi.index(self.acikKanal)
            if(cevap=="<"):
                if(self.acikKanal!=self.kanalListesi[0]):
                    self.acikKanal= self.kanalListesi[indis-1]
                    print(self.acikKanal)
            elif(cevap==">"):
                if(self.acikKanal!=self.kanalListesi[-1]):
                    self.acikKanal= self.kanalListesi[indis+1]
                    print(self.acikKanal)
            else:
                break
    def kanallariListele(self):
        print(self.kanalListesi)


kumanda=Kumanda()
print("""

1. TV aç
      
2. TV kapat
      
3. Ses Ayarlama
      
4. Kanal Ekleme
      
5. Kanal Değiştirme
      
6. Kanal Listesi
      
Çıkmak için "q" ya basın.

""")

while(True):
    islem=input("Yapmak istediğiniz işlemi seçin: ")
    if(islem=="1"):
        kumanda.tvAc()
    elif(islem=="2"):
        kumanda.tvKapat()
    elif(islem=="3"):
        kumanda.sesAyarla()
    elif(islem=="4"):
        kanal= input("Eklemek istediğiniz kanalın adını yazınız: ")
        kumanda.kanalEkle(kanal)
    elif(islem=="5"):
        kumanda.kanalDegistir()
    elif(islem=="6"):
        kumanda.kanallariListele()
    else:
        print("Programdan çıkılıyor.")
        break



