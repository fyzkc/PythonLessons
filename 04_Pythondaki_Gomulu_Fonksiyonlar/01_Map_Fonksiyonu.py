"""
Python'daki gömülü fonksiyonlar print() type() gibi fonksiyonlardır.
Şimdi de diğer gömülü fonksiyonları öğrenelim:

"""

#map() fonksiyonunun yapısı şu şekildedir:

# map(fonksiyon(),iterasyonu yapılabilecek veri tipi(liste,demet, vs...),.....)

#map fonksiyonu ilk parametre olarak bir fonksiyon alır.
#ikinci parametre olarak da liste, demet gibi bi veritipi alarak
#bu veritipinin sahip olduğu her bir elemana, gönderilen fonksiyonu uygulayarak
#sonuçları bir map objesi olarak döndürür.

def double(x):
    return x*2

liste=list()
liste= map(double,[1,2,3,4,5,6,7])
for i in liste:
    print(i)

#bunu birden fazla liste ile de kullanabiliriz:

liste1=[1,2,3,4]
liste2=[5,6,7,8]
liste3=[9,10,11,12,13]

sonuc= list(map(lambda x,y : x*y,liste1,liste2))

print("-----------------------------") #önceki sonuçla karışmasın diye
#fonksiyon tanımlamasını lambda ile de yapabiliriz.

for i in sonuc:
    print(i)

#Eğer üç listeyi birbiriyle çarpma işlemi yapsaydık, liste3 içindeki 13 elemanı
#diğer listelerden farklı olarak 5. eleman olacağı için, ilk dört eleman kendi aralarında çarpılacak,
#13 elemanı görmezden gelinecekti.

