"""
Problem 2
"şiir.txt" şeklinde bir dosya oluşturun ve içinde şu satırlar yer alsın.

                    Memlekete sis çökmüş bir gece 
                    Usulca yanağıma sen düşüyorsun
                    Sabah saat dokuzu beş geçe
                    Terk edip bizleri gidiyorsun
                    Ayrılık bu kadar yakmamıştı içimizi
                    Farkında mısın bilmiyorum
                    Aldın beraberinde cumhuriyetimizi
                    Korkunç bir veda, sararmıştı her yer
                    Ellerini uzat tutmak istiyoruz
                    Masmavi gözleri kaybetmiş çocuk
                    Aldı bir sabah ruhumuzu
                    Lakin nasıl bölmesin yokluğun uykumuzu

Bu dosyanın herbir satırını okuyun. Satırların baş harflerini birbirine ekleyerek bir string oluşturun ve bu string'i ekrana yazdırın.
"""

with open("C:/Users/Feyza/Desktop/Python Dersleri/5-Ileri Seviye Veri Yapıları ve Objeler/Onuncu Ödev - siir.txt","r",encoding="utf-8") as file:
    siir= file.read()
    satirlar= siir.split("\n")
    akrostis= ""

    # [
    # 'Memlekete sis çökmüş bir gece ', 
    # 'Usulca yanağıma sen düşüyorsun', 
    # 'Sabah saat dokuzu beş geçe', 
    # 'Terk edip bizleri gidiyorsun', 
    # 'Ayrılık bu kadar yakmamıştı içimizi', 
    # 'Farkında mısın bilmiyorum', 
    # 'Aldın beraberinde cumhuriyetimizi', 
    # 'Korkunç bir veda, sararmıştı her yer', 
    # 'E bu kadar yakmamıştı içllerini uzat tutmak istiyoruz', 
    # 'Masmavi gözleri kaybetmiş çocuk', 
    # 'Aldı bir sabah ruhumuzu', 
    # 'Lakin nasıl bölmesin yokluğun uykumuzu'
    # ]

    for i in satirlar:
        akrostis+=i[0]
            
print(akrostis)



#------------------------------------
#ÇÖZÜM: 

print("------------------------------")

bas_harfler = ""

with open("C:/Users/Feyza/Desktop/Python Dersleri/5-Ileri Seviye Veri Yapıları ve Objeler/Onuncu Ödev - siir.txt","r",encoding="utf-8") as file:
    for satır in file:
        bas_harfler += satır[0]
print(bas_harfler)



