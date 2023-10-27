from kutuphane_projesi1 import *
import time

print("Kütüphane programına hoşgeldiniz.")

print("""
***********************
      
İşlemler:
      1. Kitapları Göster
      2. Kitap Sorgulama
      3. Kitap Ekle
      4. Kitap Sil
      5. Baskı Yükselt

      Çıkmak için 'q' ya basın.

***********************

""")

kutuphane= Kutuphane()


while(True):
    islem=input("Yapmak istediğiniz işlemin numarasını yazın: ")

    if(islem=="q"):
        print("Programdan çıkılıyor.")
        time.sleep(1)
        break
    elif(islem=='1'):
        kutuphane.kitaplariGoster()
    elif(islem=='2'):
        isim= input("Kitabın ismini yazınız: ")
        print("Kitap sorgulanıyor..")
        time.sleep(1)
        kutuphane.kitapSorgula(isim)
    elif(islem=='3'):
        isim=input("Kitabın ismi: ")
        yazar= input("Kitabın yazarı: ")
        yayinevi= input("Kitabın yayınevi: ")
        tur= input("Kitabın türü: ")
        baski = int(input("Kitabın baskı numarası: "))
        #kitap classından yeniKitap isimli bir nesne oluşturduk.
        #Bu nesneyi, kütüphane classımızın içerisindeki kitapEkle()
        #fonksiyonuna parametre olarak göndereceğiz.
        yeniKitap= Kitap(isim,yazar,yayinevi,tur,baski)

        print("Kitap ekleniyor..")
        time.sleep(1)

        kutuphane.kitapEkle(yeniKitap)
        print("Kitap eklendi.")
    elif(islem=='4'):
        isim=input("Silmek istediğiniz kitabın ismini yazınız: ")
        cevap=input("Bu kitabı islmek istediğinizden emin misiniz? Bu işlem geri alınamaz! (E/H)")

        if(cevap=='E'):
            print("Kitap siliniyor..")
            time.sleep(1)
            kutuphane.kitapSil(isim)
            print("Kitap başarıyla silindi.")
        
    elif(islem=='5'):
        isim=input("Baskısını yükseltmek istediğiniz kitabın ismini yazınız: ")
        print("Kitap sorgulanıyor...")
        time.sleep(1)

        if(kutuphane.baskiYukselt(isim)==False):
            print("Baskısını yükseltmek istediğiniz kitap kayıtlarımızda bulunmamaktadır.")
        else:
            print("Kitabın baskı numarası güncelleniyor..")
            time.sleep(1)
            kutuphane.baskiYukselt(isim)
            print("İşlem başarılı.")
    else:
        print("Geçersiz işlem tuşladınız.")
        continue