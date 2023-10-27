# LİSTE OLUŞTURMA:

liste = ["elma", 35, "merhaba", 3.14, 5]

# listeler içerisinde her türden veri tipini tutabilir.

liste = []

# bu şekilde de boş bir liste tanımlayabiliriz.

liste = list()

# bu şekilde de boş bir liste oluşturabiliriz.

# len() fonksiyonuyla listelerin uzunluğunu bulabiliriz.

liste = list("Merhaba")

# Bu listeyi döndürdüğümüzde çıktı olarak şunu verir:

# ['M','e','r','h','a','b','a']

# LİSTE İŞLEMLERİ

# listeleri stringlerde olduğu gibi toplayabiliriz.

liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
liste3 = liste1+liste2

# erkan çıktısı olarak şunu verir:

# [1,2,3,4,5,6]

# listeleri bir tamsayıyla çarptığımızda, içerisindeki elemanlar çarptığımız tam sayı değeri kadar tekrarlanır.

liste1*3

# ekran çıktısı:

# [1,2,3,1,2,3,1,2,3]

# olur.

# LİSTE METOTLARI

# append() listenin sonuna eleman eklemek için kullanılır.

# pop() listenin son elemanını listeden çıkartır ve ekranda yazdırır. ancak pop(0) bu şekilde bir kullanım olursa burada belirttiğimiz indeks numarasındaki elemanı listeden çıkartır ve ekrana yazdırır.

# sort() metodu listeleri küçükten büyüğe sıralamak için kullanılır. sort(reverse= True) dersek ise listeyi büyükten küçüğe sıralarız. string elemanlar içeren listelerde ise sort() metodu alfabetik olarak sıralanır.

# İÇ İÇE LİSTELER

# listelerin içerisinde birden fazla listeyi eleman olarak verebiliriz.

liste4 = [[1, 2], [3, 4], [5, 6]]
