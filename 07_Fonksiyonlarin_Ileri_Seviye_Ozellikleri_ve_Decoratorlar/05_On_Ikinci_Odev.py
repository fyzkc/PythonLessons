"""
1'den 1000'e kadar olan asal sayıları ekrana yazdıran bir program yazın. 
Daha sonra bir tane decorator fonksiyon kullanarak bu fonksiyona 1'den 1000'e kadar olan mükemmel sayıları yazdırma özelliği ekleyin.
"""

"""
NOT: Mükemmel sayı, sayılar teorisinde, kendisi hariç pozitif tam bölenlerinin toplamı kendisine eşit olan sayı. 
"""


def mukemmelSayilar(fonksiyon):
    def wrapper(sayilar):
        
        for i in (sayilar):
            toplam=0
            if(i==0 or i==1 or i==2):
                continue
            for j in range(1,i):
                if(i%j==0):
                    toplam+=j
            if(toplam==i):
                print(i,"Bir mükemmel sayıdır.")
        fonksiyon(sayilar)
    return wrapper

#NOTLAR:
"""
decorator fonksiyonumuz içerisinde, parametre olarak gönderdiğimiz fonksiyonu, decorator fonksiyonu içerisinde çağırmazsak
parametre olarak gönderdiğimiz fonksiyonu çalıştırmamıza rağmen, yalnızca decorator fonksiyon çalışır.

yani bu örnekte, mukemmelSayilar isimli fonksiyonumuz decorator olarak kullandığımız fonksiyon.
biz daha sonrasında parametre olarak bu fonksiyona asalSayilar fonksiyonumuzu gönderiyoruz.
ancak bu fonksiyon içerisindeki wrapper fonksiyonu içinde 
fonksiyon(sayilar) 
satırını yazmazsak, asalSayilar fonksiyonunu çağırmamıza rağmen asalSayilar fonksiyonu içinde yazılanlar çalışmaz.
sadece mukemmelSayilar fonksiyonu içindekiler çalışır.

"""

@mukemmelSayilar
def asalSayilar(sayilar):
    asalMi=bool
    for i in sayilar:
        if(i==0 or i==1):
            continue
        elif(i==2):
            print(i)
        else:
            for j in range(i):
                if(j==0 or j==1):
                    continue
                else:
                    if(i%j==0):
                        asalMi=False
                        break
                    else:
                        asalMi=True
            if(asalMi==True):
                print(i)
                
            

# asalSayilar(range(15))
# asalSayilar(range(100))
asalSayilar(range(1000))


