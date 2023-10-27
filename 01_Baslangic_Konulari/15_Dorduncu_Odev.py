"""
Problem 1
1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.

Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).

Problem 2
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.

Problem için şu siteye bakabilirsiniz;

http://www.matematikciler.com/6-sinif/matematik-konu-anlatimlari/1020-en-kucuk-ortak-kat-ve-en-buyuk-ortak-bolen-ebob-ekok

Problem 3
Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.

Problem için şu siteye bakabilirsiniz;

http://www.matematikciler.com/6-sinif/matematik-konu-anlatimlari/1020-en-kucuk-ortak-kat-ve-en-buyuk-ortak-bolen-ebob-ekok

Problem 4
Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.

Örnek: 97 ---------> Doksan Yedi

Problem 5
1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)

"""

#PROBLEM 1: Mükemmel Sayılar


# sayi=int(input("Bir sayı giriniz: "))
# def bolenleriBul(sayi):
#     bolenler=[]
#     for i in range(1,sayi):
#         if(sayi%i==0):
#             bolenler.append(i)
#     return bolenler

# def basamakBul(sayi):
#     basamakSayisi=0
#     while(int(sayi%10)>0):
#         basamakSayisi+=1
#         sayi=sayi/10
#     return basamakSayisi

# def mukemmelSayiBul(a):
#     toplam=0
#     for x in bolenleriBul(sayi):
#         toplam+= x*basamakBul(sayi)
#     return toplam

# if(mukemmelSayiBul(sayi)==sayi):
#     print("Girdiğiniz sayı mükemmel bir sayıdır.")
# else:
#     print("Girdiğiniz sayı mükemmel bir sayı değildir.")

#PROBLEM 2: EBOB

# sayi1=int(input("Birinci sayıyı giriniz: "))
# sayi2=int(input("İkinci sayıyı giriniz: "))

# def bolenleriBul(sayi):
#     bolenler=[]
#     for i in range(1,sayi+1):
#         if(sayi%i==0):
#             bolenler.append(i)
#     return bolenler


# def ebob(a,b):
#     ortakBolenler=[]
#     for x in a: 
#         for y in b:
#             if(x==y):
#                 ortakBolenler.append(y)
#     return max(ortakBolenler)

# sonuc=ebob(bolenleriBul(sayi1),bolenleriBul(sayi2))

# print("Girdiğiniz sayıların ebobu: ",sonuc)


#PROBLEM 3: EKOK

# sayi1=int(input("Birinci sayıyı giriniz: ")) #6 
# sayi2=int(input("İkinci sayıyı giriniz: ")) #8 


# def ekok(a,b):
#     sayi1=a
#     sayi2=b
#     katlar1=[a]
#     katlar2=[b]
#     for i in katlar1:
#         if(i in katlar2):
#             return i
#         a+=sayi1 #12
#         b+=sayi2 #16
#         katlar1.append(a)
#         katlar2.append(b)

# value=ekok(sayi1,sayi2)
# print("Girdiğiniz sayıların ekoku: ", value)


#PROBLEM 4: Sayıların Okunuşu

# sayi=int(input("Lütfen iki basamaklı bir sayı giriniz: "))

# # sayilar=[0,1,2,3,4,5,6,7,8,9]
# birinciSayi=""
# ikinciSayi=""

# while(sayi/10==0):
#     sayi=input("Lütfen iki basamaklı bir sayı giriniz: ")

# def okunus(a): #sayı 35 olsun 35/10=3 olur ve bu da onlar basamağını verir. 35%10=5 bu da birler basamağını verir.
#     global birinciSayi
#     global ikinciSayi
#     deger=a
#     if(int(a/10)==1):
#         birinciSayi="On "
#         a=deger%10
#     elif(int(a/10)==2):
#         birinciSayi="Yirmi "
#         a=deger%10
#     elif(int(a/10)==3):
#         birinciSayi="Otuz "
#         a=deger%10
#     elif(int(a/10)==4):
#         birinciSayi="Kırk "
#         a=deger%10
#     elif(int(a/10)==5):
#         birinciSayi="Elli "
#         a=deger%10
#     elif(int(a/10)==6):
#         birinciSayi="Altmış "
#         a=deger%10
#     elif(int(a/10)==7):
#         birinciSayi="Yetmiş "
#         a=deger%10
#     elif(int(a/10)==8):
#         birinciSayi="Seksen "
#         a=deger%10
#     else:
#         birinciSayi="Doksan "
#         a=deger%10
        
#     if(a==1):
#         ikinciSayi="Bir"
#     elif(a==2):
#         ikinciSayi="İki"
#     elif(a==3):
#         ikinciSayi="Üç"
#     elif(a==4):
#         ikinciSayi="Dört"
#     elif(a==5):
#         ikinciSayi="Beş"
#     elif(a==6):
#         ikinciSayi="Altı"
#     elif(a==7):
#         ikinciSayi="Yedi"
#     elif(a==8):
#         ikinciSayi="Sekiz"
#     elif(a==9):
#         ikinciSayi="Dokuz"
#     else:
#         ikinciSayi=""
    
#     return birinciSayi + ikinciSayi
        

# value=okunus(sayi)
# print(value)


#PROBLEM 5: Pisagor Üçlüsü

#Pisagor üçgeni oluşturan sayılar, a^2 + b^2 = c^2 eşitliğini sağlayan sayılardır.

# def pisagor():
#     sayilar=[]
#     for i in range(1,101): 
#         for j in range(1,i): 
#             for k in range(1,j): 
#                 if(k**2 +j**2==i**2):
#                     sayilar.append((k,j,i))
#     return sayilar


# value= pisagor()
# print(value)

