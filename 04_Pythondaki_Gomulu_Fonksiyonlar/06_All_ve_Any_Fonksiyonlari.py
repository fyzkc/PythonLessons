#öncelikle şu işlemi yapmaya çalışalım:

#Elimizde bir fonksiyonumuz olsun. Bu fonksiyon parametre olarak bir liste alsın.
#Bu liste içerisinde True veya False değerleri olsun.
#Eğer liste içerisinde en az bir tane False değer varsa, fonksiyon False değer döndürsün.
#Ancak liste içerisinde hiç false değer yoksa fonksiyon True döndürsün:

def hepsi(liste):
    for i in liste:
        if not i: #i false ise
            return False
    return True #hiç false yoksa döngü biter, bu yüzden true döndürür.

liste=[True,False,True,False,True]

print(hepsi(liste))

#Bu şekilde listeyi gönderdiğimizde, içerisinde en az bir tane bile False değeri olduğu için
#False değeri döndürür.

liste2=[1,2,3,4,5]

print(hepsi(liste2))

#NOT: Sayılarda 0 hariç bütün sayıların değeri True olarak döner.

#Bu yüzden bu listeyi gönderdiğimizde sonucumuz true döner.

#Bir de bu fonksiyonun tam tersi işlevi yapan, yani;
#Listedeki elemanların hepsi False olduğunda False dönen, en az bir tane True olduğunda True dönen bir fonksiyon olsun.

def herhangi(liste):
    for i in liste:
        if i:
            return True
    return False

liste=[True,False,True,False,True]
print(herhangi(liste))
#True döner

liste=[0,0,0,0,0]
print(herhangi(liste))
#False döner.


#Yukarıda yaptığımız işlemleri kolayca yapan fonksiyonlar all() ve any() fonksiyonlarıdır.

#all() fonksiyonu: eğer bütün değerler true ise true, en az bir false değer varsa false sonucunu döndürür.

liste=[True,False,True,False,True]
print(all(liste)) #False döner.

liste=[True,True,True]
print(all(liste)) #True döner.

#any() fonksiyonu: eğer bütün değerler false ise false, en az bir true değer varsa true döndürür.

liste=[True,False,True,False,True]
print(any(liste)) #True döner.

liste=[0,0,0,0,0]
print(any(liste)) #False döner.
