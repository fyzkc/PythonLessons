"""
Elinizde "mailler.txt" adında , maillerin ve bazı yazıların bulunduğu bir dosya olsun. 
Bu dosyanın her bir satırını okuyun ve sadece mail formatına uygun olanları ekrana yazdırın.

                    coskun.m.murat@gmail.com
                    example@xyz.com
                    mustafa.com
                    mustafa@gmail
                    kerim@yahoo.com

                           //
                           //
                           //


*İpucu: Stringlerde bulunan endswith ve find metodlarını kullanabilirsiniz.*
"""

with open("C:/Users/Feyza/Desktop/Python Dersleri/5-Ileri Seviye Veri Yapıları ve Objeler/mailler.txt","r",encoding="utf-8") as file:
    icerik = file.read()
    satirlar=icerik.split("\n")
    mailler=list()

    for i in satirlar:
        if(i.find("@")!=-1 and i.endswith(".com")==True):
            mailler.append(i)

    for a in mailler:
        print(a)

#------------------------------------
#ÇÖZÜM: 

print("------------------------------")

with open("C:/Users/Feyza/Desktop/Python Dersleri/5-Ileri Seviye Veri Yapıları ve Objeler/mailler.txt","r",encoding="utf-8") as file:
    for satır in file:
        satır = satır[:-1]
        if (satır.endswith(".com")==True and satır.find("@") != -1):
            print(satır)