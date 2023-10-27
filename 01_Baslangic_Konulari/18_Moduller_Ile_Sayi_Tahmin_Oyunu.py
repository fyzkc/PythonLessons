import random
import time

print("Sayı tahmin oyununa hoşgeldiniz.")

print("1 ile 40 arasında bir sayı tahmin etmeniz isteniyor.\nVe yalnızca 7 tahmin hakkınız bulunmaktadır.")

rastgeleSayi = random.randint(1,40)
#1 ve 40 sayılarını da dahil ederek 1 ile 40 arasında bir rastgele sayı oluşturur.


tahminHakki=7
while(True):
    tahmin=int(input("Tahmininiz: "))
    if(tahmin<rastgeleSayi):
        print("Tahmininiz kontrol ediliyor...")
        time.sleep(1)
        #sleep fonksiyonu programı 1 saniyeliğine uyutur.
        print("Daha yüksek bir sayı tahmin edin.")
        tahminHakki-=1
    elif(tahmin>rastgeleSayi):
        print("Tahmininiz kontrol ediliyor...")
        time.sleep(1)
        print("Daha düşük bir sayı tahmin edin.")
        tahminHakki-=1
    else:
        print("Tahmininiz kontrol ediliyor...")
        time.sleep(1)
        print("Tebrikler doğru tahmin ettiniz: ",rastgeleSayi)
        break
    if(tahminHakki==0):
        print("Tahmin hakkınız bitti, doğru cevap: ",rastgeleSayi)
        break


