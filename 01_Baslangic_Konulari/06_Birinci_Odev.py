"""
PROBLEM1: Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini "format" metoduyla yapmaya çalışın.

PROBLEM2: Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
NOT: Beden kitle indeksi = Kilo/Boy^2 ile hesaplanır.

PROBLEM3: Bir aracın kilometrede ne kadar yaktığını ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünün toplam ne kadar ödemesi gerektiğini hesaplayın.

PROBLEM4: Kullanıcıdan ad, soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.

PROBLEM5: Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

PROBLEM6: Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) isteyin ve hipotenüsünü bulmaya çalışın.
NOT: Hipotenüs= a^2+b^2=c^2
"""

# PROBLEM1:
# ---------------------------------------------

birinci_sayi = int(input("Birinci sayıyı giriniz: "))
ikinci_sayi = int(input("İkinci sayıyı giriniz: "))
ucuncu_sayi = int(input("Üçüncğ sayıyı giriniz: "))

carpim = birinci_sayi*ikinci_sayi*ucuncu_sayi

print("Sayıların çarpımı: {}".format(carpim))


# PROBLEM2
# ---------------------------------------------

boy = float(input("Boyunuzu girin: "))
kilo = int(input("Kilonuzu girin: "))
bki = kilo/(boy**2)
print("Beden kitle indeksiniz: ", bki)


# PROBLEM3
# ---------------------------------------------

# 1 litre= 10TL olsun.

fiyat = 10
litre = int(input("Kilometre başına kaç lt yakıt yaktığınızı giriniz: "))
km = int(input("Kaç kilometre gittiğinizi giriniz: "))

km_basina_tl = litre*fiyat
# km başına yakılan lt fiyatı

toplam_km_tl = km_basina_tl*km

print("Ödemeniz gereken fiyat: {}".format(toplam_km_tl))


# PROBLEM4
# ---------------------------------------------

ad = input("Adınızı girin: ")
soyad = input("Soyadınızı girin: ")
numara = int(input("Numaranızı girin: "))

print("Ad: {}\nSoyad: {}\nNumara: {}".format(ad, soyad, numara))


# PROBLEM5
# ---------------------------------------------

sayi1 = int(input("Birinci sayı: "))
sayi2 = int(input("İkinci sayı: "))

print("Sayıların yerlerini değiştirelim")
sayi1, sayi2 = sayi2, sayi1
print("Birinci sayı: {}\nİkinci sayı: {} ".format(sayi1, sayi2))


# PROBLEM6
# ---------------------------------------------

birinci_kenar = int(input("Üçgenin birinci dik kenarını girin: "))
ikinci_kenar = int(input("Üçgenin ikinci dik kenarını girin: "))

hipotenus = (birinci_kenar**2+ikinci_kenar**2)**(1/2)

print("Hipotenüs uzunluğu: {}".format(hipotenus))
