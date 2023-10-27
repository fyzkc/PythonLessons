liste=["Elma","Armut","Muz","Kiraz"]

#elimizde böyle bir listemiz olsun.
#Bu listenin her bir elemanını bir indis değeriyle birlikte
#gruplandırmak isteyelim:

#[(0,'Elma'),(1,'Armut'),(2,'Muz'),(3,'Kiraz')]

i=0
sonuc=list()
while(i<len(liste)):
    sonuc.append((i,liste[i]))
    i+=1

print(sonuc)

#biz bu işlemi daha kolay bir şekilde enumerate fonksiyonu ile yapabiliriz:

print("-----------------")
print(list(enumerate(liste)))

#Bu şekilde tek bir satırda bu işlemi halledebiliriz:

#Yine oluşturduğumuz bu liste üzerinde enumerate fonksiyonu sayesinde
#tek bir for döngüsü ile gezinebiliriz:

print("-----------------")

for i,j in enumerate(liste):
    print(i,j)


