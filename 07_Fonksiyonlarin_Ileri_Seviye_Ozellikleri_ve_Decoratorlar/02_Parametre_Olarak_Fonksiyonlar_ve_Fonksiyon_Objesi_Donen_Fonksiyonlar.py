#Fonksiyon Olarak Dönmek ve Argüman Olarak Göndermek

#Fonksiyonları return ile dönmek:

def anafonksiyon(islemAdi):
    def toplama(*args):
        toplam=0
        for i in args:
            toplam+=i
        return toplam
    def carpma(*args):
        carpim=1
        for i in args:
            carpim*= i
        return carpim
    if(islemAdi=="toplama"):
        return toplama #toplama fonksiyonumuzu döndürdük.
    else:
        return carpma #carpma fonksiyonumuzu döndürdük.
    
fonk=anafonksiyon("toplama")
#burada fonk objesi toplama fonksiyonuna eşit olur ve bu fonksiyonu artık toplama fonksiyonu gibi kullanabiliriz.

print(fonk(1,2,3,4,5))
#15

fonk2=anafonksiyon("çarpma")
#burada da fonk2 fonksiyonu çarpma fonksiyonuna eşit olur ve bu fonksiyonu artık çarpma fonksiyonu gibi kullanabiliriz.

print(fonk2(1,2,3))
#6

#Fonksiyonları argüman olarak gönderme:

def toplama(a,b):
    return a+b
def cikarma(a,b):
    if(a>b):
        return a-b
    else:
        return b-a
def carpma(a,b):
    return a*b
def bolme(a,b):
    if(b!=0):
        return a/b
    
def anaFonksiyon(func1,func2,func3,func4,islemAdi):
    if(islemAdi=="toplama"):
        print(func1(3,4))
    elif(islemAdi=="çıkarma"):
        print(func2(10,3))
    elif(islemAdi=="çarpma"):
        print(func3(3,5))
    elif(islemAdi=="bölme"):
        print(func4(10,5))
    else:
        print("Geçersiz işlem.")

anaFonksiyon(toplama,cikarma,carpma,bolme,"toplama")
#7
anaFonksiyon(toplama,cikarma,carpma,bolme,"çarpma")
#15