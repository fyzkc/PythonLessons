#öncelikle bir liste içerisindeki elemanları nasıl gruplayabileceğimize bir göz atalım:

liste1=[1,2,3,4,5]
liste2=[6,7,8,9,10,11]

#Bu iki listeyi birleştirip, 
# [(1,6),(2,7),(3,8),(4,9),(5,10)]
#şeklinde bir liste içerisinde demet şekilde tutmaya çalışalım.

#11 sayısı fazla olduğu ve onunla gruplaşacak başka eleman olmadığı için
#onu göz ardı ediyoruz.

i=0
liste3=list()
while(i<len(liste1) and i<len(liste2)):
    liste3.append((liste1[i],liste2[i]))
    i+=1

print(liste3)


#biz bu işlemi, daha kolay yapabilmek için zip fonksiyonunu kullanabiliriz.

yeni=list(zip(liste1,liste2))
print(yeni)

#Bu işlemin sonucunda da yine aynı sonucu elde etmiş oluruz.

#Bu fonksiyonu sadece integer değerlerle değil, aynı zamanda hem integer hem de string değerlerle de kullanabiliriz.

liste1=[1,2,3,4,5]
liste2=[6,7,8,9,10,11]
liste3=["Python","Java","C#","Javascript"]

print("------------------------")
print(list(zip(liste1,liste2,liste3)))

#normalde bu oluşan yeni liste içerisinde demet ile oluşturulmuş olan veritipinin elemanları içerisinde gezinmek için:

print("-----------------------------")
liste1=[1,2,3,4,5]
liste2=["Python","Java","C#","Javascript"]

sonuc=list(zip(liste1,liste2))
print(sonuc)

#[(1, 'Python'), (2, 'Java'), (3, 'C#'), (4, 'Javascript')]

for i in sonuc:
    for j in i:
        print(j, end=" ")
    print("")

#bu şekilde iç içe iki ayrı for döngüsü kurmamız gerekecekti.

#Ancak zip fonksiyonu kullanarak bunu tek for döngüsü kullanarak gerçekleştirebiliriz:

print("-----------------------------")

for i,j in zip(liste1,liste2):
    print(i,j)

print("-----------------------------")

#zip fonksiyonu kullanarak sözlükleri de gruplayabiliriz.

sozluk1= {"Elma":1,"Armut":2,"Kiraz":3}
sozluk2={"Sıfır":0,"Bir":1,"İki":2}

print(list(zip(sozluk1,sozluk2)))

#Sonuc:
# [('Elma', 'Sıfır'), ('Armut', 'Bir'), ('Kiraz', 'İki')]

#Görüldüğü gibi yalnızca anahtarları gruplar.
#Eğer biz değerleri gruplamak istersek:

print(list(zip(sozluk1.values(),sozluk2.values())))

#values() ile değerleri almış oluruz.

