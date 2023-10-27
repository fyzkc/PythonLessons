#append(): listenin en sonuna eleman eklemeyi sağlar.

#extend(): bir listeye başka bir listenin elemanlarını aktarır.

#liste1.extend(liste2)
#liste2'nin elemanlarını liste1'e atar.

#insert(): verilen index değerine eleman eklemeyi sağlar.

#liste.insert(2,"Python")
#listenin 2. indisine Python elemanını ekler.

#pop(): içine hiç bir parametre verilmediğinde listenin en sonundaki elemanı listeden çıkartır
#ve ekrana bu elemanı yazdırır. Ancak silinecek elemanın index değeri parametre olarak verilirse,
#bu indexteki elemanı siler ve yine ekrana yazdırır.

#remove(): silinmek istenen elemanın ismi parametre olarak vererek bu elemanın silinmesi sağlanır.
#eğer olmayan bir eleman ismi parametre olarak verilirse, hata verir.

#index(): parametre olarak verilen değeri liste içerisinde baştan itibaren arar ve bulduğu ilk index değerini döndürür.
#eğer öyle bir eleman yoksa hata verir. Index değeri verilerek kullanılırsa da, verilen index değerinden itibaren aramaya başlar.

#index(x,y): x: aranacak değer, y: aramaya başlanacak index


#count(): verilen değerin listede kaç kere geçtiğini sayar ve o sayıyı döndürür.

#NOT: listelerde kullanılan count metodunda, stringlerde kullanılandan farklı olarak, belli bir indexten sonra sayma işlemi yapılamaz.

#sort(): listedeki elemanları sayıysa küçükten büyüğe, string ise alfabetik olarak sıralar.
#Eğer reverse=True parametresi verilirse, tam tersi olarak sıralar.