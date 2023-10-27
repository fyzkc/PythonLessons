"""

Proje 1
--------------------------------
Bir tane "Bilgisayar" sınıfı oluşturarak bu sınıfa metodlar ve özellikler ekleyin ve bu class'ı kullanmaya çalışın.

Bu sınıfı yazarken öğrendiğimiz özel metodların hepsini tanımlamaya çalışın.

"""
from os import system
import time

class Bilgisayar():
    def __init__(self,marka,model,renk,depolama,ram,isletimSistemi,masaustu=[],cdisk=[],ddisk=[],belgeler=[],resimler=[],muzikler=[]):
        self.marka=marka
        self.model=model
        self.renk=renk
        self.depolama=depolama
        self.ram=ram
        self.isletimSistemi=isletimSistemi
        self.masaustu=masaustu #1
        self.cdisk=cdisk #2
        self.ddisk=ddisk #3 
        self.belgeler=belgeler #4
        self.resimler=resimler #5
        self.muzikler=muzikler #6

    def BilgisayarKapat(self):
        print(self.marka,"kapanıyor...")

    def KlasorleriGoruntule(self,konum):
        if(konum==1):
            if(len(self.masaustu)==0):
                print("Bu konumda hiç klasör yok.")
            else:
                print(self.masaustu)
        elif(konum==2):
            if(len(self.cdisk)==0):
                print("Bu konumda hiç klasör yok.")
            else:
                print(self.cdisk)
        elif(konum==3):
            if(len(self.ddisk)==0):
                print("Bu konumda hiç klasör yok.")
            else:
                print(self.ddisk)
        elif(konum==4):
            if(len(self.belgeler)==0):
                print("Bu konumda hiç klasör yok.")
            else:
                print(self.belgeler)
        elif(konum==5):
            if(len(self.resimler)==0):
                print("Bu konumda hiç klasör yok.")
            else:
                print(self.resimler)
        elif(konum==6):
            if(len(self.muzikler)==0):
                print("Bu konumda hiç klasör yok.")
            else:
                print(self.muzikler)
        else:
            print("Doğru bir dosya yolu seçtiğinizden emin olun..")

    def YeniKlasorOlustur(self,klasorAdi,konum):
        if(konum==1):
            #konum=="Masaüstü" or konum =="Masaustu" or konum=="masaüstü" or konum=="masaustu"
            self.masaustu.append(klasorAdi)
            print("Yeni klasör Masaüstü konumuna oluşturuldu.")
            print("Masaüstü/",self.masaustu)
        elif(konum==2):
            #konum=="C" or konum=="c" or konum =="C Diski" or konum=="C Disk" or konum=="Cdisk" or konum=="cdisk" or konum=="Cdiski" or konum=="cdiski"
            self.cdisk.append(klasorAdi)
            print("Yeni klasör C Diski konumuna oluşturuldu.")
            print("C/",self.cdisk)
        elif(konum==3):
            #konum=="D" or konum=="d" or konum =="D Diski" or konum=="D Disk" or konum=="Ddisk" or konum=="ddisk" or konum=="Ddiski" or konum=="ddiski"
            self.ddisk.append(klasorAdi)
            print("Yeni klasör D Diski konumuna oluşturuldu.")
            print("D/",self.ddisk)
        elif(konum==4):
            #konum=="Belgeler" or konum=="belgeler"
            self.belgeler.append(klasorAdi)
            print("Yeni klasör Belgeler konumuna oluşturuldu.")
            print("Belgeler/",self.belgeler)
        elif(konum==5):
            #konum=="Resimler" or konum=="resimler"
            self.resimler.append(klasorAdi)
            print("Yeni klasör Resimler konumuna oluşturuldu.")
            print("Resimler/",self.resimler)
        elif(konum==6):
            #konum=="Müzikler" or konum=="müzikler" or konum =="Muzikler" or konum=="muzikler"
            self.muzikler.append(klasorAdi)
            print("Yeni klasör Müzikler konumuna oluşturuldu.")
            print("Müzikler/",self.muzikler)
        else:
            print("Doğru bir dosya yolu yazdığınızdan emin olun..")

    def KlasorTasi(self,klasorAdi,konum):
        if(konum==1):
            if(klasorAdi in self.masaustu):
                print("Bu klasör zaten masaüstünde mevcut.")
            else:
                if(klasorAdi in self.cdisk):
                    self.cdisk.remove(klasorAdi)
                    self.masaustu.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: Masaüstü")
                    print("Masaüstü/",self.masaustu)
                elif(klasorAdi in self.ddisk):
                    self.ddisk.remove(klasorAdi)
                    self.masaustu.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: Masaüstü")
                    print("Masaüstü/",self.masaustu)
                elif(klasorAdi in self.belgeler):
                    self.belgeler.remove(klasorAdi)
                    self.masaustu.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: Masaüstü")
                    print("Masaüstü/",self.masaustu)
                elif(klasorAdi in self.resimler):
                    self.resimler.remove(klasorAdi)
                    self.masaustu.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: Masaüstü")
                    print("Masaüstü/",self.masaustu)
                elif(klasorAdi in self.muzikler):
                    self.muzikler.remove(klasorAdi)
                    self.masaustu.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: Masaüstü")
                    print("Masaüstü/",self.masaustu)
                else:
                    print("Bahsettiğiniz gibi bir klasör bulunmamaktadır.")

        elif(konum==2):
            if(klasorAdi in self.cdisk):
                print("Bu klasör zaten C Diskinde mevcut.")
            else:
                if(klasorAdi in self.masaustu):
                    self.masaustu.remove(klasorAdi)
                    self.cdisk.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: C")
                    print("C/",self.cdisk)
                elif(klasorAdi in self.ddisk):
                    self.ddisk.remove(klasorAdi)
                    self.cdisk.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: C")
                    print("C/",self.cdisk)
                elif(klasorAdi in self.belgeler):
                    self.belgeler.remove(klasorAdi)
                    self.cdisk.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: C")
                    print("C/",self.cdisk)
                elif(klasorAdi in self.resimler):
                    self.resimler.remove(klasorAdi)
                    self.cdisk.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: C")
                    print("C/",self.cdisk)
                elif(klasorAdi in self.muzikler):
                    self.muzikler.remove(klasorAdi)
                    self.cdisk.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: C")
                    print("C/",self.cdisk)
                else:
                    print("Bahsettiğiniz gibi bir klasör bulunmamaktadır.")

        elif(konum==3):
            if(klasorAdi in self.ddisk):
                print("Bu klasör zaten D Diskinde mevcut.")
            else:
                if(klasorAdi in self.masaustu):
                    self.masaustu.remove(klasorAdi)
                    self.ddisk.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: D")
                    print("D/",self.ddisk)
                elif(klasorAdi in self.cdisk):
                    self.cdisk.remove(klasorAdi)
                    self.ddisk.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: D")
                    print("D/",self.ddisk)
                elif(klasorAdi in self.belgeler):
                    self.belgeler.remove(klasorAdi)
                    self.ddisk.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: D")
                    print("D/",self.ddisk)
                elif(klasorAdi in self.resimler):
                    self.resimler.remove(klasorAdi)
                    self.ddisk.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: D")
                    print("D/",self.ddisk)
                elif(klasorAdi in self.muzikler):
                    self.muzikler.remove(klasorAdi)
                    self.ddisk.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: D")
                    print("D/",self.ddisk)
                else:
                    print("Bahsettiğiniz gibi bir klasör bulunmamaktadır.")
        elif(konum==4):
            if(klasorAdi in self.belgeler):
                print("Bu klasör zaten Belgelerde mevcut.")
            else:
                if(klasorAdi in self.masaustu):
                    self.masaustu.remove(klasorAdi)
                    self.belgeler.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: Belgeler")
                    print("Belgeler/",self.belgeler)
                elif(klasorAdi in self.cdisk):
                    self.cdisk.remove(klasorAdi)
                    self.belgeler.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: Belgeler")
                    print("Belgeler/",self.belgeler)
                elif(klasorAdi in self.ddisk):
                    self.ddisk.remove(klasorAdi)
                    self.cdisk.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: Belgeler")
                    print("Belgeler/",self.belgeler)
                elif(klasorAdi in self.resimler):
                    self.resimler.remove(klasorAdi)
                    self.belgeler.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: Belgeler")
                    print("Belgeler/",self.belgeler)
                elif(klasorAdi in self.muzikler):
                    self.muzikler.remove(klasorAdi)
                    self.belgeler.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: Belgeler")
                    print("Belgeler/",self.belgeler)
                else:
                    print("Bahsettiğiniz gibi bir klasör bulunmamaktadır.")
        elif(konum==5):
            if(klasorAdi in self.resimler):
                print("Bu klasör zaten Resimlerde mevcut.")
            else:
                if(klasorAdi in self.masaustu):
                    self.masaustu.remove(klasorAdi)
                    self.resimler.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: Resimler")
                    print("Resimler/",self.resimler)
                elif(klasorAdi in self.cdisk):
                    self.cdisk.remove(klasorAdi)
                    self.resimler.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: Resimler")
                    print("Resimler/",self.resimler)
                elif(klasorAdi in self.ddisk):
                    self.ddisk.remove(klasorAdi)
                    self.resimler.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: Resimler")
                    print("Resimler/",self.resimler)
                elif(klasorAdi in self.belgeler):
                    self.belgeler.remove(klasorAdi)
                    self.resimler.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: Resimler")
                    print("Resimler/",self.resimler)
                elif(klasorAdi in self.muzikler):
                    self.muzikler.remove(klasorAdi)
                    self.resimler.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: Resimler")
                    print("Resimler/",self.resimler)
                else:
                    print("Bahsettiğiniz gibi bir klasör bulunmamaktadır.")
        elif(konum==6):
            if(klasorAdi in self.muzikler):
                print("Bu klasör zaten Müzkilerde mevcut.")
            else:
                if(klasorAdi in self.masaustu):
                    self.masaustu.remove(klasorAdi)
                    self.muzikler.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: Müzikler")
                    print("Müzikler/",self.muzikler)
                elif(klasorAdi in self.cdisk):
                    self.cdisk.remove(klasorAdi)
                    self.muzikler.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: Müzikler")
                    print("Müzikler/",self.muzikler)
                elif(klasorAdi in self.ddisk):
                    self.ddisk.remove(klasorAdi)
                    self.muzikler.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: Müzikler")
                    print("Müzikler/",self.muzikler)
                elif(klasorAdi in self.belgeler):
                    self.belgeler.remove(klasorAdi)
                    self.muzikler.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: Müzikler")
                    print("Müzikler/",self.muzikler)
                elif(klasorAdi in self.resimler):
                    self.resimler.remove(klasorAdi)
                    self.muzikler.append(klasorAdi)
                    print("Klasör taşındı. Klasörün yeni konumu: Müzikler")
                    print("Müzikler/",self.muzikler)
                else:
                    print("Bahsettiğiniz gibi bir klasör bulunmamaktadır.")
        else:
            print("Doğru bir dosya yolu yazdığınızdan emin olun..")


    def KlasorKopyala(self,klasorAdi,konum):
        if(konum==1):
            self.masaustu.append(klasorAdi)
            print("Klasör kopyalandı: Masaüstü")
            print("Masaüstü/",self.masaustu)
        elif(konum==2):
            self.cdisk.append(klasorAdi)
            print("Klasör kopyalandı: C")
            print("C/",self.cdisk)
        elif(konum==3):
            self.ddisk.append(klasorAdi)
            print("Klasör kopyalandı: D")
            print("D/",self.ddisk)
        elif(konum==4):
            self.belgeler.append(klasorAdi)
            print("Klasör kopyalandı: Belgeler")
            print("Belgeler/",self.belgeler)
        elif(konum==5):
            self.resimler.append(klasorAdi)
            print("Klasör kopyalandı: Resimler")
            print("Resimler/",self.resimler)
        elif(konum==6):
            self.muzikler.append(klasorAdi)
            print("Klasör kopyalandı: Müzikler")
            print("Müzikler/",self.muzikler)
        else:
            print("Doğru bir dosya yolu yazdığınızdan emin olun..")

    def KlasorSil(self,klasorAdi):
        if(klasorAdi in self.masaustu):
            self.masaustu.remove(klasorAdi)
            print("Klasör silindi.")
        elif(klasorAdi in self.cdisk):
            self.cdisk.remove(klasorAdi)
            print("Klasör silindi.")
        elif(klasorAdi in self.ddisk):
            self.ddisk.remove(klasorAdi)
            print("Klasör silindi.")
        elif(klasorAdi in self.belgeler):
            self.belgeler.remove(klasorAdi)
            print("Klasör silindi.")
        elif(klasorAdi in self.resimler):
            self.resimler.remove(klasorAdi)
            print("Klasör silindi.")
        elif(klasorAdi in self.muzikler):
            self.muzikler.remove(klasorAdi)
            print("Klasör silindi.")
        else:
            print("Doğru bir klasör adı yazdığınızdan emin olun..")

    def SistemOzellikleri(self):
        print("Marka: {}\nModel: {}\nRenk: {}\nDepolama: {}\nRam: {}\nİşletim Sistemi: {}".format(self.marka,self.model,self.renk,self.depolama,self.ram,self.isletimSistemi))
    


bilgisayar=Bilgisayar("Asus","Zenbook","Gümüş","128 GB","8 GB","Windows 10")

while(True):
    print("1-Bilgisayarı Kapat\n2-Klasörleri Görüntüle\n3-Yeni Klasör Oluştur\n4-Klasör Taşı\n5-Klasör Kopyala\n6-Klasör Sil\n7-Sistem Özelliklerini görüntüle")
    islem=int(input("Lütfen yapmak istediğiniz işlemi seçin: "))
    

    if(islem==1):
        system("cls")
        bilgisayar.BilgisayarKapat()
        time.sleep(5)
        system("cls")
        break
    elif(islem==2):
        konum=int(input("Klasörleri görüntülemek istediğiniz konumu seçiniz:\n1-Masaüstü\n2-C Diski\n3-D Diski\n4-Belgeler\n5-Resimler\n6-Müzikler\n"))
        system("cls")
        bilgisayar.KlasorleriGoruntule(konum)
        islem2=input("Ana menüye dönmek için 'q' ya basın.\n")
        if(islem2=="q"):
            system("cls")
            continue
    elif(islem==3):
        ad=input("Lütfen yeni oluşturacağınız klasörün adını yazınız: ")
        konum=int(input("Klasörü oluşturmak istediğiniz konumu seçiniz:\n1-Masaüstü\n2-C Diski\n3-D Diski\n4-Belgeler\n5-Resimler\n6-Müzikler\n"))
        system("cls")
        bilgisayar.YeniKlasorOlustur(ad,konum)
        islem2=input("Ana menüye dönmek için 'q' ya basın.\n")
        if(islem2=="q"):
            system("cls")
            continue
    elif(islem==4):
        ad=input("Taşımak istediğiniz klasörün adını yazınız: ")
        konum=int(input("Klasörü nereye taşımak istediğinizi seçiniz:\n1-Masaüstü\n2-C Diski\n3-D Diski\n4-Belgeler\n5-Resimler\n6-Müzikler\n"))
        system("cls")
        bilgisayar.KlasorTasi(ad,konum)
        islem2=input("Ana menüye dönmek için 'q' ya basın.\n")
        if(islem2=="q"):
            system("cls")
            continue
    elif(islem==5):
        ad=input("Kopyalamak istediğiniz klasörün adını yazınız: ")
        konum=int(input("Klasörü nereye kopyalamak istediğinizi seçiniz:\n1-Masaüstü\n2-C Diski\n3-D Diski\n4-Belgeler\n5-Resimler\n6-Müzikler\n"))
        system("cls")
        bilgisayar.KlasorKopyala(ad,konum)
        islem2=input("Ana menüye dönmek için 'q' ya basın.\n")
        if(islem2=="q"):
            system("cls")
            continue
    elif(islem==6):
        ad=input("Silmek istediğiniz klasörün adını yazınız:\n")
        system("cls")
        bilgisayar.KlasorSil(ad)
        islem2=input("Ana menüye dönmek için 'q' ya basın.\n")
        if(islem2=="q"):
            system("cls")
            continue
    elif(islem==7):
        system("cls")
        bilgisayar.SistemOzellikleri()
        islem2=input("Ana menüye dönmek için 'q' ya basın.\n")
        if(islem2=="q"):
            system("cls")
            continue
    else:
        print("Doğru bir işlem seçtiğinizden emin olun.")
        islem2=input("Ana menüye dönmek için 'q' ya basın.\n")
        if(islem2=="q"):
            system("cls")
            continue