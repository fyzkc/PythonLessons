# Proje 3
# https://www.doviz.com/ sitesinden anlık olarak doların,euronun,altının ve borsanın değerlerini öğrenin 
# ve bunları kullanarak bir proje geliştirmeye çalışın.

# *Not: Bu projeyi, requests ve beautifulsoup kullanarak geliştirin.*

import requests
from bs4 import BeautifulSoup
from os import system
import time

# para_birimi = soup.find_all("span",{"class":"name"})
# para_degeri = soup.find_all("span",{"class":"value"})


# for birim,deger in zip(para_birimi,para_degeri):
#     birim = birim.text
#     deger = deger.text

#     birim=birim.strip() #boşlukları silelim
#     birim=birim.replace("\n","") #\n yerine boşluk karakteri koyduk.

#     deger=deger.strip()
#     deger=deger.replace("\n","") 

#     #NOT: strip ve replace metodunu kullandıktan sonra yeni stringi başka bir değişkene atamazsak çalışmaz

#     print("Para Birimi:",birim)
#     print("Para Değeri:",deger,"TL")


# Para Birimi: GRAM ALTIN
# Para Değeri: 1.653,56 TL
# Para Birimi: DOLAR
# Para Değeri: 27,1606 TL
# Para Birimi: EURO
# Para Değeri: 29,6248 TL
# Para Birimi: STERLİN
# Para Değeri: 34,6625 TL
# Para Birimi: BIST 100
# Para Değeri: 7.637,83 TL
# Para Birimi: BITCOIN
# Para Değeri: $26.017 TL
# Para Birimi: GRAM GÜMÜŞ
# Para Değeri: 20,22 TL
# Para Birimi: BRENT
# Para Değeri: $85,48 TL

print("Döviz Hesaplama Programına Hoşgeldiniz.")
time.sleep(2)

while(True):

    response = requests.get("https://www.doviz.com/")

    html_icerigi = response.content
    soup = BeautifulSoup(html_icerigi,"html.parser")

    para_altin = soup.find_all("span",attrs={"class":"value","data-socket-key":"gram-altin"})
    for altin in para_altin:
        altin = altin.text
        altin = altin.replace(".","")
        altin = altin.replace(",",".")
        altinfloat=float(altin)

    para_usd = soup.find_all("span",attrs={"class":"value","data-socket-key":"USD"})
    for usd in para_usd:
        usd = usd.text
        usd = usd.replace(".","")
        usd = usd.replace(",",".")
        usdfloat=float(usd)

    para_eur = soup.find_all("span",attrs={"class":"value","data-socket-key":"EUR"})
    for eur in para_eur:
        eur = eur.text
        eur = eur.replace(".","")
        eur = eur.replace(",",".")
        eurfloat=float(eur)

    para_sterlin = soup.find_all("span",attrs={"class":"value","data-socket-key":"GBP"})
    for sterlin in para_sterlin:
        sterlin = sterlin.text
        sterlin = sterlin.replace(".","")
        sterlin = sterlin.replace(",",".")
        sterlinfloat=float(sterlin)

    para_btc = soup.find_all("span",attrs={"class":"value","data-socket-key":"bitcoin"})
    for btc in para_btc:
        btc = btc.text
        btc = btc.replace(".","")
        btc = btc.replace(",",".")
        btc = btc.replace("$","")
        btcfloat=float(btc)

    para_gumus = soup.find_all("span",attrs={"class":"value","data-socket-key":"gumus"})
    for gumus in para_gumus:
        gumus = gumus.text
        gumus = gumus.replace(".","")
        gumus = gumus.replace(",",".")
        gumusfloat=float(gumus)

    birinciPara= input("Birinci para birimini girin: ")
    ikinciPara= input("İkinci para birimini girin: ")


   #NOT: GRAM ALTINDAN DİĞER PARA BİRİMLERİNE DÖNÜŞÜM İŞLEMLERİ:

    if(birinciPara == "GRAM ALTIN" or birinciPara == "Gram Altın" or birinciPara=="gram altın" or birinciPara == "altın" or birinciPara == "Altın" or birinciPara == "ALTIN"):
        if(ikinciPara =="TL" or ikinciPara == "TRY" or ikinciPara == "Türk Lirası" or ikinciPara =="tl"):
            #gram altının birin fiyatı altinfloat değişkeni içerisindeki değer.
            gram = float(input("TL'ye çevirmek istediğiniz altın gramını giriniz: "))
            print(gram,"gram altın",gram*altinfloat,"Türk Lirası değerindedir.")
            
        elif(ikinciPara=="Dolar" or ikinciPara== "dolar" or ikinciPara =="DOLAR" or ikinciPara == "USD" or ikinciPara=="usd"):
            gram = float(input("USD'ye çevirmek istediğiniz altın gramını giriniz: "))
            #NOT: 1 gram altın x tl, 1 dolar y tl ise, 1 gram altın x/y dolar değerindedir.
            print(gram,"gram altın",gram*(altinfloat/usdfloat),"Amerikan Doları değerindedir.")
            
        elif(ikinciPara=="Euro" or ikinciPara=="EURO" or ikinciPara=="euro" or ikinciPara=="EUR" or ikinciPara =="eur" or ikinciPara=="Eur" or ikinciPara =="avro" or ikinciPara=="Avro" or ikinciPara =="AVRO"):
            gram = float(input("Euro'ya çevirmek istediğiniz altın gramını giriniz: "))
            print(gram,"gram altın",gram*(altinfloat/eurfloat),"Euro değerindedir.")
            
        elif(ikinciPara=="Sterlin" or ikinciPara=="sterlin" or ikinciPara == "STERLİN" or ikinciPara == "STERLIN" or ikinciPara=="Pound" or ikinciPara == "POUND" or ikinciPara=="pound"):
            gram = float(input("Sterlin'e çevirmek istediğiniz altın gramını giriniz: "))
            print(gram,"gram altın",gram*(altinfloat/sterlinfloat),"İngiliz Sterlini değerindedir.")
            
        elif(ikinciPara=="Bitcoin" or ikinciPara == "bitcoin" or ikinciPara== "BİTCOİN" or ikinciPara == "BITCOIN" or ikinciPara == "btc" or ikinciPara == "Btc" or ikinciPara=="BTC"):
            gram = float(input("Bitcoin'e çevirmek istediğiniz altın gramını giriniz: "))
            #1 bitcoinin dolar cinsinden değeri verildiğinden önce onu tl ye çevirelim.
            #1 btc x dolar, 1 dolar y tl ise, 1 btc x*y tl değerindedir.
            print(gram,"gram altın",gram*(altinfloat/(btcfloat*usdfloat)),"Bitcoin değerindedir.")
            
        elif(ikinciPara=="GRAM GÜMÜŞ" or ikinciPara == "Gram Gümüş" or ikinciPara == "gram gümüş" or ikinciPara =="GÜMÜŞ" or ikinciPara == "Gümüş" or ikinciPara == "gümüş"):
            gram = float(input("Gümüş'e çevirmek istediğiniz altın gramını giriniz: "))
            print(gram,"gram altın",gram*(altinfloat/gumusfloat),"Gümüş değerindedir.")


    #NOT: DOLARDAN DİĞER PARA BİRİMLERİNE DÖNÜŞÜM İŞLEMLERİ:

    elif(birinciPara =="Dolar" or birinciPara== "dolar" or birinciPara =="DOLAR" or birinciPara == "USD" or birinciPara=="usd" ):
        if(ikinciPara=="TL" or ikinciPara == "TRY" or ikinciPara == "Türk Lirası" or ikinciPara =="tl"):
            dolar = float(input("TL'ye çevirmek istediğiniz dolar miktarını giriniz: "))
            print(dolar,"Dolar",dolar*usdfloat,"Türk Lirası değerindedir.")
        elif(ikinciPara == "GRAM ALTIN" or ikinciPara == "Gram Altın" or ikinciPara=="gram altın" or ikinciPara == "altın" or ikinciPara == "Altın" or ikinciPara == "ALTIN"):
            dolar = float(input("Gram altına çevirmek istediğiniz dolar miktarını giriniz: "))
            print(dolar,"Dolar",dolar*(usdfloat/altinfloat),"Gram Altın değerindedir.")
        elif(ikinciPara=="Euro" or ikinciPara=="EURO" or ikinciPara=="euro" or ikinciPara=="EUR" or ikinciPara =="eur" or ikinciPara=="Eur" or ikinciPara =="avro" or ikinciPara=="Avro" or ikinciPara =="AVRO"):
            dolar = float(input("EURO'ya çevirmek istediğiniz dolar miktarını giriniz: "))
            print(dolar,"Dolar",dolar*(usdfloat/eurfloat),"Euro değerindedir.")
        elif(ikinciPara=="Sterlin" or ikinciPara=="sterlin" or ikinciPara == "STERLİN" or ikinciPara == "STERLIN" or ikinciPara=="Pound" or ikinciPara == "POUND" or ikinciPara=="pound"):
            dolar = float(input("Sterlin'e çevirmek istediğiniz dolar miktarını giriniz: "))
            print(dolar,"Dolar",dolar*(usdfloat/sterlinfloat),"İngiliz Sterlini değerindedir.")
        elif(ikinciPara=="Bitcoin" or ikinciPara == "bitcoin" or ikinciPara== "BİTCOİN" or ikinciPara == "BITCOIN" or ikinciPara == "btc" or ikinciPara == "Btc" or ikinciPara=="BTC"):
            dolar = float(input("Bitcoin'e çevirmek istediğiniz dolar miktarını giriniz: "))
            print(dolar,"Dolar",dolar*(usdfloat/btcfloat),"Bitcoin değerindedir.")
        elif(ikinciPara=="GRAM GÜMÜŞ" or ikinciPara == "Gram Gümüş" or ikinciPara == "gram gümüş" or ikinciPara =="GÜMÜŞ" or ikinciPara == "Gümüş" or ikinciPara == "gümüş"):
            dolar = float(input("Gümüşe çevirmek istediğiniz dolar miktarını giriniz: "))
            print(dolar,"Dolar",dolar*(usdfloat/gumusfloat),"gram gümüş değerindedir.")


    #NOT: TÜRK LİRASINDAN DİĞER PARA BİRİMLERİNE DÖNÜŞÜM İŞLEMLERİ:

    elif(birinciPara =="TL" or birinciPara == "TRY" or birinciPara == "Türk Lirası" or birinciPara =="tl"):
        if(ikinciPara == "GRAM ALTIN" or ikinciPara == "Gram Altın" or ikinciPara=="gram altın" or ikinciPara == "altın" or ikinciPara == "Altın" or ikinciPara == "ALTIN"):
            tl = float(input("Gram altına çevirmek istediğiniz Türk Lirası miktarını giriniz: "))
            print(tl,"TL",tl/altinfloat,"Gram Altın değerindedir.")
        elif(ikinciPara=="Dolar" or ikinciPara== "dolar" or ikinciPara =="DOLAR" or ikinciPara == "USD" or ikinciPara=="usd"):
            tl = float(input("Dolar'a çevirmek istediğiniz Türk Lirası miktarını giriniz: "))
            print(tl,"TL",tl/usdfloat,"Amerikan Doları değerindedir.")
        elif(ikinciPara=="Euro" or ikinciPara=="EURO" or ikinciPara=="euro" or ikinciPara=="EUR" or ikinciPara =="eur" or ikinciPara=="Eur" or ikinciPara =="avro" or ikinciPara=="Avro" or ikinciPara =="AVRO"):
            tl = float(input("Euro'ya çevirmek istediğiniz Türk Lirası miktarını giriniz: "))
            print(tl,"TL",tl/eurfloat,"Euro değerindedir.")
        elif(ikinciPara=="Sterlin" or ikinciPara=="sterlin" or ikinciPara == "STERLİN" or ikinciPara == "STERLIN" or ikinciPara=="Pound" or ikinciPara == "POUND" or ikinciPara=="pound"):
            tl = float(input("Sterlin'e çevirmek istediğiniz Türk Lirası miktarını giriniz: "))
            print(tl,"TL",tl/sterlinfloat,"İngiliz Sterlini değerindedir.")
        elif(ikinciPara=="Bitcoin" or ikinciPara == "bitcoin" or ikinciPara== "BİTCOİN" or ikinciPara == "BITCOIN" or ikinciPara == "btc" or ikinciPara == "Btc" or ikinciPara=="BTC"):
            tl = float(input("Bitcoin'e çevirmek istediğiniz Türk Lirası miktarını giriniz: "))
            print(tl,"TL",tl/(btcfloat*usdfloat),"Bitcoin değerindedir.")
        elif(ikinciPara=="GRAM GÜMÜŞ" or ikinciPara == "Gram Gümüş" or ikinciPara == "gram gümüş" or ikinciPara =="GÜMÜŞ" or ikinciPara == "Gümüş" or ikinciPara == "gümüş"):
            tl = float(input("Gümüşe çevirmek istediğiniz Türk Lirası miktarını giriniz: "))
            print(tl,"TL",tl/gumusfloat,"gram gümüş değerindedir.")


    #NOT: EURODAN DİĞER PARA BİRİMLERİNE DÖNÜŞÜM İŞLEMLERİ:

    elif(birinciPara=="Euro" or birinciPara=="EURO" or birinciPara=="euro" or birinciPara=="EUR" or birinciPara =="eur" or birinciPara=="Eur" or birinciPara =="avro" or birinciPara=="Avro" or birinciPara =="AVRO"):
        if(ikinciPara=="TL" or ikinciPara == "TRY" or ikinciPara == "Türk Lirası" or ikinciPara =="tl"):
            euro = float(input("TL'ye çevirmek istediğiniz euro miktarını giriniz: "))
            print(euro,"EURO",euro*eurfloat,"Türk Lirası değerindedir.")
        elif(ikinciPara == "GRAM ALTIN" or ikinciPara == "Gram Altın" or ikinciPara=="gram altın" or ikinciPara == "altın" or ikinciPara == "Altın" or ikinciPara == "ALTIN"):
            euro = float(input("Gram Altına çevirmek istediğiniz euro miktarını giriniz: "))
            print(euro,"EURO",euro*(eurfloat/altinfloat),"gram altın değerindedir.")
        elif(ikinciPara=="Dolar" or ikinciPara== "dolar" or ikinciPara =="DOLAR" or ikinciPara == "USD" or ikinciPara=="usd"):
            euro = float(input("Dolar'a çevirmek istediğiniz euro miktarını giriniz: "))
            print(euro,"EURO",euro*(eurfloat/usdfloat),"Amerikan Doları değerindedir.")
        elif(ikinciPara=="Sterlin" or ikinciPara=="sterlin" or ikinciPara == "STERLİN" or ikinciPara == "STERLIN" or ikinciPara=="Pound" or ikinciPara == "POUND" or ikinciPara=="pound"):
            euro = float(input("Sterlin'e çevirmek istediğiniz euro miktarını giriniz: "))
            print(euro,"EURO",euro*(eurfloat/sterlinfloat),"İngiliz Sterlini değerindedir.")
        elif(ikinciPara=="Bitcoin" or ikinciPara == "bitcoin" or ikinciPara== "BİTCOİN" or ikinciPara == "BITCOIN" or ikinciPara == "btc" or ikinciPara == "Btc" or ikinciPara=="BTC"):
            euro = float(input("Bitcoin'e çevirmek istediğiniz euro miktarını giriniz: "))
            print(euro,"EURO",euro*(eurfloat/(btcfloat*usdfloat)),"Bitcoin değerindedir.")
        elif(ikinciPara=="GRAM GÜMÜŞ" or ikinciPara == "Gram Gümüş" or ikinciPara == "gram gümüş" or ikinciPara =="GÜMÜŞ" or ikinciPara == "Gümüş" or ikinciPara == "gümüş"):
            euro = float(input("Gümüşe çevirmek istediğiniz euro miktarını giriniz: "))
            print(euro,"EURO",euro*(eurfloat/gumusfloat),"gram gümüş değerindedir.")


    #NOT: STERLINDEN DİĞER PARA BİRİMLERİNE DÖNÜŞÜM İŞLEMLERİ:

    elif(birinciPara=="Sterlin" or birinciPara=="sterlin" or birinciPara == "STERLİN" or birinciPara == "STERLIN" or birinciPara=="Pound" or birinciPara == "POUND" or birinciPara=="pound"):
        if(ikinciPara=="TL" or ikinciPara == "TRY" or ikinciPara == "Türk Lirası" or ikinciPara =="tl"):
            strln = float(input("TL'ye çevirmek istediğiniz Sterlin miktarını giriniz: "))
            print(strln,"Sterlin",strln*sterlinfloat,"Türk Lirası değerindedir.")
        elif(ikinciPara == "GRAM ALTIN" or ikinciPara == "Gram Altın" or ikinciPara=="gram altın" or ikinciPara == "altın" or ikinciPara == "Altın" or ikinciPara == "ALTIN"):
            strln = float(input("Gram altına çevirmek istediğiniz Sterlin miktarını giriniz: "))
            print(strln,"Sterlin",strln*(sterlinfloat/altinfloat),"gram altın değerindedir.")
        elif(ikinciPara=="Dolar" or ikinciPara== "dolar" or ikinciPara =="DOLAR" or ikinciPara == "USD" or ikinciPara=="usd"):
            strln = float(input("Dolar'a çevirmek istediğiniz Sterlin miktarını giriniz: "))
            print(strln,"Sterlin",strln*(sterlinfloat/usdfloat),"Amerikan Doları değerindedir.")
        elif(ikinciPara=="Euro" or ikinciPara=="EURO" or ikinciPara=="euro" or ikinciPara=="EUR" or ikinciPara =="eur" or ikinciPara=="Eur" or ikinciPara =="avro" or ikinciPara=="Avro" or ikinciPara =="AVRO"):
            strln = float(input("EURO'ya çevirmek istediğiniz Sterlin miktarını giriniz: "))
            print(strln,"Sterlin",strln*(sterlinfloat/eurfloat),"EURO değerindedir.")
        elif(ikinciPara=="Bitcoin" or ikinciPara == "bitcoin" or ikinciPara== "BİTCOİN" or ikinciPara == "BITCOIN" or ikinciPara == "btc" or ikinciPara == "Btc" or ikinciPara=="BTC"):
            strln = float(input("Bitcoin'e çevirmek istediğiniz Sterlin miktarını giriniz: "))
            print(strln,"Sterlin",strln*(sterlinfloat/(btcfloat*usdfloat)),"Bitcoin değerindedir.")
        elif(ikinciPara=="GRAM GÜMÜŞ" or ikinciPara == "Gram Gümüş" or ikinciPara == "gram gümüş" or ikinciPara =="GÜMÜŞ" or ikinciPara == "Gümüş" or ikinciPara == "gümüş"):
            strln = float(input("Gümüşe çevirmek istediğiniz Sterlin miktarını giriniz: "))
            print(strln,"Sterlin",strln*(sterlinfloat/gumusfloat),"gram gümüş değerindedir.")
            

    #NOT: BITCOINDEN DİĞER PARA BİRİMLERİNE DÖNÜŞÜM İŞLEMLERİ:
  
    elif(birinciPara=="Bitcoin" or birinciPara == "bitcoin" or birinciPara== "BİTCOİN" or birinciPara == "BITCOIN" or birinciPara == "btc" or birinciPara == "Btc" or birinciPara=="BTC"):
        if(ikinciPara=="TL" or ikinciPara == "TRY" or ikinciPara == "Türk Lirası" or ikinciPara =="tl"):
            btcoin = float(input("TL'ye çevirmek istediğiniz Bitcoin miktarını giriniz: "))
            print(btcoin,"Bitcoin",btcoin*(btcfloat*usdfloat),"Türk Lirası değerindedir.")
        elif(ikinciPara == "GRAM ALTIN" or ikinciPara == "Gram Altın" or ikinciPara=="gram altın" or ikinciPara == "altın" or ikinciPara == "Altın" or ikinciPara == "ALTIN"):
            btcoin = float(input("Gram altına çevirmek istediğiniz Bitcoin miktarını giriniz: "))
            print(btcoin,"Bitcoin",btcoin*((btcfloat*usdfloat)/altinfloat),"gram altın değerindedir.")
        elif(ikinciPara=="Dolar" or ikinciPara== "dolar" or ikinciPara =="DOLAR" or ikinciPara == "USD" or ikinciPara=="usd"):
            btcoin = float(input("Dolara çevirmek istediğiniz Bitcoin miktarını giriniz: "))
            print(btcoin,"Bitcoin",btcoin*btcfloat,"Amerikan Doları değerindedir.")
        elif(ikinciPara=="Euro" or ikinciPara=="EURO" or ikinciPara=="euro" or ikinciPara=="EUR" or ikinciPara =="eur" or ikinciPara=="Eur" or ikinciPara =="avro" or ikinciPara=="Avro" or ikinciPara =="AVRO"):
            btcoin = float(input("EURO'ya çevirmek istediğiniz Bitcoin miktarını giriniz: "))
            print(btcoin,"Bitcoin",btcoin*((btcfloat*usdfloat)/eurfloat),"EURO değerindedir.")
        elif(ikinciPara=="Sterlin" or ikinciPara=="sterlin" or ikinciPara == "STERLİN" or ikinciPara == "STERLIN" or ikinciPara=="Pound" or ikinciPara == "POUND" or ikinciPara=="pound"):
            btcoin = float(input("Sterlin'e çevirmek istediğiniz Bitcoin miktarını giriniz: "))
            print(btcoin,"Bitcoin",btcoin*((btcfloat*usdfloat)/sterlinfloat),"İngiliz Sterlini değerindedir.")
        elif(ikinciPara=="GRAM GÜMÜŞ" or ikinciPara == "Gram Gümüş" or ikinciPara == "gram gümüş" or ikinciPara =="GÜMÜŞ" or ikinciPara == "Gümüş" or ikinciPara == "gümüş"):
            btcoin = float(input("Gümüşe çevirmek istediğiniz Bitcoin miktarını giriniz: "))
            print(btcoin,"Bitcoin",btcoin*((btcfloat*usdfloat)/gumusfloat),"gram gümüş değerindedir.")
            

    #NOT: GRAM GÜMÜŞTEN DİĞER PARA BİRİMLERİNE DÖNÜŞÜM İŞLEMLERİ:
  
    elif(birinciPara=="GRAM GÜMÜŞ" or birinciPara == "Gram Gümüş" or birinciPara == "gram gümüş" or birinciPara =="GÜMÜŞ" or birinciPara == "Gümüş" or birinciPara == "gümüş"):
        if(ikinciPara=="TL" or ikinciPara == "TRY" or ikinciPara == "Türk Lirası" or ikinciPara =="tl"):
            gram = float(input("TL'ye çevirmek istediğiniz gümüş gramını giriniz: "))
            print(gram,"gram gümüş",gram*gumusfloat,"Türk Lirası değerindedir.")
        elif(ikinciPara == "GRAM ALTIN" or ikinciPara == "Gram Altın" or ikinciPara=="gram altın" or ikinciPara == "altın" or ikinciPara == "Altın" or ikinciPara == "ALTIN"):
            gram = float(input("Gram altına çevirmek istediğiniz gümüş gramını giriniz: "))
            print(gram,"gram gümüş",gram*(gumusfloat/altinfloat),"gram altın değerindedir.")
        elif(ikinciPara=="Dolar" or ikinciPara== "dolar" or ikinciPara =="DOLAR" or ikinciPara == "USD" or ikinciPara=="usd"):
            gram = float(input("Dolara çevirmek istediğiniz gümüş gramını giriniz: "))
            print(gram,"gram gümüş",gram*(gumusfloat/usdfloat),"Amerikan Doları değerindedir.")
        elif(ikinciPara=="Euro" or ikinciPara=="EURO" or ikinciPara=="euro" or ikinciPara=="EUR" or ikinciPara =="eur" or ikinciPara=="Eur" or ikinciPara =="avro" or ikinciPara=="Avro" or ikinciPara =="AVRO"):
            gram = float(input("EURO'ya çevirmek istediğiniz gümüş gramını giriniz: "))
            print(gram,"gram gümüş",gram*(gumusfloat/eurfloat),"EURO değerindedir.")
        elif(ikinciPara=="Sterlin" or ikinciPara=="sterlin" or ikinciPara == "STERLİN" or ikinciPara == "STERLIN" or ikinciPara=="Pound" or ikinciPara == "POUND" or ikinciPara=="pound"):
            gram = float(input("Sterlin'e çevirmek istediğiniz gümüş gramını giriniz: "))
            print(gram,"gram gümüş",gram*(gumusfloat/sterlinfloat),"İngiliz Sterlini değerindedir.")
        elif(ikinciPara=="Bitcoin" or ikinciPara == "bitcoin" or ikinciPara== "BİTCOİN" or ikinciPara == "BITCOIN" or ikinciPara == "btc" or ikinciPara == "Btc" or ikinciPara=="BTC"):
            gram = float(input("Bitcoin'e çevirmek istediğiniz gümüş gramını giriniz: "))
            print(gram,"gram gümüş",gram*(gumusfloat/(btcfloat*usdfloat)),"Bitcoin değerindedir.")
