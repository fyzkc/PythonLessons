#string metotları:

#upper() ve lower() :
#upper fonksiyonu tüm karakterleri büyük harf yapar.
#lower fonksiyonu ise tüm karakterleri küçük harf yapar.

#replace(x,y): 
#x ve y değerlerini birbiriyle değiştirir.

print("Bütün ü'leri döndür".replace("ü","a"))
# Batan a'leri döndar


#startswith() ve endswith():

#startswith(x): string x karakteriyle başlıyorsa true, değilse false döndürür.
#endswith(x): string x karakteriyle bitiyorsa true, değilse false döndürür.

#NOT: Büyük küçük harf duyarlılığı var.

#NOT: Kelimenin son bir kaç hecesi veya ilk bir kaç hecesi verildiğinde de true döner.

print("python".endswith("on"))
#True döner.

print("Python".startswith("Pyt"))
#True döner.

#split(x):
#stringi x karakterine göre ayırır ve ayrılan her bir parça bir listeye atılır.

liste="Python programlama dili".split(" ")
print(liste)
#['Python', 'programlama', 'dili']

#strip(x), lstrip(x), rstrip(x):

#strip(x): stringin başında ve sonunda bulunan x değerlerini siler.
#lstrip(x): stringin sadece başında bulunan x değerlerini siler.
#rstrip(x): stringin sadece sonunda bulunan x değerlerini siler.

#NOT: Default olarak x değeri boşluk karakteridir.

#join(): 
#listenin her bir elemanını verilen bir stringle birleştirerek yeni bir string oluşturur.

liste=["21","02","2014"]
print("/".join(liste))

#count():
#bu fonksiyonun iki türlü kullanımı vardır:
#count(x): x karakterinin string içerisinde kaç defa geçtiğini döndürür.
#count(x,index): verilen index değerinden sonra x karakterinin string içerisinde kaç defa geçtiğini sayar ve sonucu döndürür.


#find() ve rfind():
#find(x): x değerini bütün string içerisinde baştan başlayarak arar ve bulursa ilk bulduğu index değerini, bulamazsa -1 değerini döndürür.
#rfind(x): x değerini bütün string içerisinde sondan başlayarak arar ve bulursa ilk bulduğu index değerini, bulamazsa -1 değerini döndürür.

