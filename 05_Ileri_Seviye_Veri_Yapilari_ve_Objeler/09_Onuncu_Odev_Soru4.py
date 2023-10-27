"""
Problem 4
Elinizde 2 tane liste bulunsun. Bu listelerden isim ve soyisimleri birleştirerek , ekrana isim ve soyisimleri *isimlere* göre 
sıralı bir şekilde yazdırmaya çalışın.

        isim -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

        soyisim ------> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
"""

isim= ["Kerim","Tarık","Ezgi","Kemal","Ilkay","Şükran","Merve"]
soyisim= ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

isimler = list(zip(isim,soyisim))

print(isimler)

isimler.sort()

for i,j in isimler:
    print(i,j)

#---------------------------------------------------

#ÇÖZÜM: 

print("---------------------------------------------")

isim = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

soyisim = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

liste = list(zip(isim,soyisim))

liste.sort()

for i,j in liste:
    print(i,j)
