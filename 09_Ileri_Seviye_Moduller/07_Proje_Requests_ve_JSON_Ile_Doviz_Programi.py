"""
fixer.io sitesinden bilgilerimizi json objesi olarak alıp,
bu bilgilerle Dolar'ı Türk lirasına çevirme gibi işlemleri gerçekleştireceğiz.

"""

#Json objeleri pythondaki sözlüklere benzerler.

#Örnek Json objesi:

# {
#     "İsim": "Feyza",
#     "Soyisim": "Koç",
#     "Numara": 12345,
#     "Özellikler": 
#     {
#         "hobi": "Gitar Çalmak",
#         "iş": "Bilgisayar Mühendisi"
#     }

# }

import requests
import sys
url= "http://data.fixer.io/api/latest?base="


#NOT: Site ücretli üyelik istediğinden sonuçları elde edemeyeceğim,
#ama yine de kodları öğrenmek açısından yazıyorum.

birinciDoviz=input("Birinci Döviz:")
ikinciDoviz=input("İkinci Döviz:")

response= requests.get(url+birinciDoviz)
#url içerisindeki base kısmından sonraki kısma, kullanıcının girdiği
#birinci dövizi ekledik.

print(response)

jsonverisi=response.json()
#içerikten dönen verileri json objesine çevirdik.

print(jsonverisi["rates"])
#rates sözcüğü, içerik içindeki birinci dövizi base olarak verdiğimizde,
#diğer para birimlerindeki karşılıklarıdır.
#Bu şekilde USD birimine karşılık gelen bütün diğer para birimleri listelenir.

print(jsonverisi["rates"][ikinciDoviz])
#burada da diğer para birimleri arasından bizim girdiğimiz değeri,
#rates içerisinden çekip, değerini ekrana yazdırdık.
#Yani örneğin birinciDovize USD ve ikinciDovize TRY girersek,
#USD'nin TRY'ye karşılığını ekranda görmüş oluruz.

miktar=float(input("Miktar:"))
#Kullanıcıdan dönüştürmek istediği para miktarını yazmasını istiyoruz.

print(jsonverisi["rates"][ikinciDoviz]) * miktar
#Girilen miktara göre, paranın diğer para birimindeki karşılığını,
#birim fiyatı üzerinden çarparak buluyoruz.

#Eğer var olmayan bir para birimi girilirse diye bu işlemi
#hata blokları içerisinde yapabiliriz.

try:
    print(jsonverisi["rates"][ikinciDoviz]) * miktar
except KeyError:
    sys.stderr.write("Böyle bir para birimi yok.")
    sys.stderr.flush()
