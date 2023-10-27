#PROBLEM 1: MÜKEMMEL SAYI

# def mukemmel(sayi):
#     toplam=0
#     for i in range(1,sayi):
#         if(sayi%i==0):
#             toplam+=i
#     return toplam==sayi

# for i in range(1,1001):
#     if(mukemmel(i)):
#         print("Mükemmel Sayı: ",i)

#PROBLEM 2: EBOB

# def ebobBulma(sayi1,sayi2):
#     i=1
#     ebob=1
#     while(i<=sayi1 and i<=sayi2):
#         if(not (sayi1%i)and not (sayi2%i)):
#             ebob=i
#         i+=1
#     return ebob

# sayi1=int(input("Sayı-1: "))
# sayi2=int(input("Sayı-2: "))

# print("Ebob: ",ebobBulma(sayi1,sayi2))

#PROBLEM 3: EKOK

# def ekok_bulma(sayı1,sayı2):
    
#     i = 2
#     ekok = 1
#     while True:
#         if (sayı1 % i == 0 and sayı2 % i == 0):
#             ekok *= i

#             sayı1 //= i
#             sayı2 //= i


#         elif (sayı1 % i ==  0 and sayı2 % i != 0):
#             ekok *= i

#             sayı1 //= i


#         elif (sayı1 % i != 0 and sayı2 % i == 0):
#             ekok *= i

#             sayı2 //= i
#         else:
#             i += 1
#         if (sayı1 == 1 and sayı2 == 1):
#             break
#     return ekok

# sayı1 = int(input("Sayı-1:"))
# sayı2 = int(input("Sayı-2:"))

# print("Ekok:",ekok_bulma(sayı1,sayı2))


#PROBLEM 4: SAYI OKUNUŞU

# birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
# onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

# def okunus(sayı):
#     birinci = sayı % 10
#     ikinci = sayı // 10
    
#     return onlar[ikinci] + " " + birler[birinci]

    
# sayı =  int(input("Sayı:"))

# print(okunus(sayı))

#PROBLEM 5: PİSAGOR ÜÇLÜSÜ:

# def pisagor_bulma():
    
#     pisagor_listesi = list()
#     for i in range(1,101):
#         for j in range(1,101):

#             c = (i ** 2 + j ** 2) ** 0.5

#             if (c == int(c) ):
#                 pisagor_listesi.append((i,j,int(c)))

#     return pisagor_listesi

# for i in pisagor_bulma():
#     print(i)
