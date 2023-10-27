"""
Oluşabilecek bazı hatalara karşı, derleme sırasında sorun yaşamamak için, programı çalıştırabileceğimiz ve 
hatanın neyden kaynaklandığını bildiren mesajlar görebileceğimiz hata yakalamayı kullanabiliriz.

"""

# try-except-finally blokları

# try:
#     Hata çıkarabilecek kodlar
# except:
#     Hata çıkması durumunda gerçekleşecek olan kodlar
    
try:
    a=int("sdsfds45322")
except:
    print("Bir hata oluştu!!") 

#Burada özellikle bir hata belirtilmediği için her ne olursa olsun except bloğuna girecektir.

#Ancak hatanın türü verilerek birden fazla except bloğu kullanabilir ve hangi hatanın hangi
#except bloğuna gireceğine karar verebiliriz.

try:
    print("Birinci try bloğu")
    a=int("sjdg2645732")
    #b=2/0
except ValueError:
    print("Girilen ifade 10'luk tabanda değil!")
except ZeroDivisionError:
    print("Sıfıra bölünme hatası!")

try:
    print("İkinci try bloğu")
    #a=int("sjdg2645732")
    b=2/0
except ValueError:
    print("Girilen ifade 10'luk tabanda değil!")
except ZeroDivisionError:
    print("Sıfıra bölünme hatası!")


#İki ayrı hatayı tek except bloğunda da birleştirebiliriz.

try:
    a=int(input("Sayı 1:"))
    b=int(input("Sayı 2:"))
    print(a/b)
except(ValueError,ZeroDivisionError):
    print("Doğru bir sayı girdiğinizden veya ikinci sayının 0 olmadığından emin olun!")


# finally blokları:
#finally bloğu, hata oluşsa da oluşmasa da mutlaka çalışacak olan kodlaır içerir.
#finally bloğu except bloğundan sonra tanımlanır.

