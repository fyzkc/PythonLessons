"""
Dosya okumak ve dosyalardan veri almak için "r" kipiyle açmamız gerekir.
Bu kiple dosyalar varsa açılır, yoksa python tarafından FileNotFound hatası verir.
Bu hataları try-except bloklarıyla yakalayabiliriz.

"""

file= open("C:/Users/Feyza/Desktop/Python Dersleri/3-Dosya Islemleri/bilgiler.txt","r")

file.close()

#For döngüsü ile dosyayı okuma:

file= open("C:/Users/Feyza/Desktop/Python Dersleri/3-Dosya Islemleri/bilgiler.txt","r",encoding="utf-8")

for i in file:
    print(i)
file.close()

#Tıpkı listelerde olduğu gibi listenin her bir satırında gezinme yapabiliriz.
#Ve her bir satırı sırasıyla ekrana bastırabiliriz.

#Bu kodun çıktısı olarak, daha önceden txt dosyamızın içerisinde biz yazarken \n ile
#bir alt satıra inmiştik ve print fonksiyonu kendisi de her işlemde bir alt satıra indiği için 
#her bir satır arasında bir satır boşlukla ekrana yazdırır.
#bunu önlemek için print fonksiyonuna end="" parametresi ekleyebiliriz.

file= open("C:/Users/Feyza/Desktop/Python Dersleri/3-Dosya Islemleri/bilgiler.txt","r",encoding="utf-8")

for i in file:
    print(i,end="")
file.close()

#Bu şekilde satırlar arasında bir satır boşluk bırakmadan alt alta yazdırabiliriz.

# read() fonksiyonu

#read() fonksiyonu içerisinde hiç bir değer vermezsek bütün dosyamızı okuyacaktır.
#read() fonksiyonuna değer vererek dosyanın belirli bir kısmını okumayı daha sonra öğrenelim.


file= open("C:/Users/Feyza/Desktop/Python Dersleri/3-Dosya Islemleri/bilgiler.txt","r",encoding="utf-8")

icerik= file.read()
print("Dosya içeriği:\n",icerik,sep="")
file.close()

# readline() fonksiyonu

#Bu fonksiyon dosyanın sadece tek satırını okur.
#Ve her çağırıldığında en son okuduğu satırdan sonrasını okur.

# readlines() fonksiyonu

#Bu fonksiyon her bir satırı okuyarak bir listeye atar.

file= open("C:/Users/Feyza/Desktop/Python Dersleri/3-Dosya Islemleri/bilgiler.txt","r",encoding="utf-8")
liste= file.readlines()
print(liste)
file.close()


