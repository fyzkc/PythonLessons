def ekstra(fonksiyon):
    def wrapper(sayilar):
        cifttoplami=0 #çift sayıların toplamı
        ciftsayilar=0 #çift sayıların sayısı
        tektoplami=0 #tek sayıların toplamı
        teksayilar=0 #tek sayıların sayısı

        for i in sayilar:
            if(i%2==0):
                cifttoplami+=i
                ciftsayilar+=1
            else:
                tektoplami+=i
                teksayilar+=1
        print("Tek sayıların ortalaması:",tektoplami/teksayilar)
        print("Çift sayıların ortalaması:",ciftsayilar/ciftsayilar)

        fonksiyon(sayilar)
    return wrapper

@ekstra
def ortalamaBul(sayilar):
    toplam=0
    for i in sayilar:
        toplam+=i
    print("Genel Ortalama:",toplam/len(sayilar))

ortalamaBul([1,2,3,4,34,60,63,32,100,105])
#Genel Ortalama: 40.4 (Decorator fonksiyonu tanımlanmadan önce)
"""
Tek sayıların ortalaması: 43.0
Çift sayıların ortalaması: 1.0
Genel Ortalama: 40.4
"""
#(Decorator fonksiyonu tanımlandıktan sonra)

