#filter() fonksiyonunun yapısı:

# filter(fonksiyon,(liste,demet vb.))

#filter fonksiyonunun ilk aldığı parametre olan fonksiyonun 
#mutlaka True veya False bir değer dönmesi gerekir.

#filter fonksiyonları, mantıksal bir değer döndüren bir fonksiyon ile
#iterasyon yapılabilecek bir veritipini parametre olarak alır.
#veritipi üzerine fonksiyonu uyguladıktan sonra yalnızca true değer çıkanları
#bir filter objesi olarak döndürür.

ciftSayi=list(filter(lambda x: x%2==0, [1,2,3,4,5,6,7,8,9,10]))
print(ciftSayi)

#Bu şekilde sadece çift sayı olanları döndürür.

#Asal sayı bulma:

def asalMi(x):
    i=2
    if(x==1):
        return False
    elif(x==2):
        return True
    else:
        while(i<x):
            if(x%i==0):
                return False
            i+=1
        return True
asalSayilar= list(filter(asalMi,range(1,100)))

print(asalSayilar)