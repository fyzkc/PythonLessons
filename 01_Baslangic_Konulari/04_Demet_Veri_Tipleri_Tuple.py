# demetler (tuple'lar), listelerden farklı olarak değiştirilemezlerdir.

demet = (1, 2, 3, 4, 5, 6, 7)
print(type(demet))

# tuple çıktısını verir.

print(demet[4])

# 5 çıktısını verir.

# DEMETLERİN METOTLARI

# demetlerin yalnızca iki metodu vardır:

# count() fonksiyonu, içerisine verilen parametredeki değerin demet içerisinde kaç defa kullanıldığını döndürür.

demet2 = (1, 1, 1, 1, 1, 4, 4, 4, 6, 6, 8)
print(demet2.count(1))

# 5 çıktısını verir.

# index() metodu parametre olarak verilen değerin demet içerisinde kaçıncı indekste olduğunu döndürür. demet içerisinde olmayan bir değeri aratmaya çalıştığımızda ise error verir.

demet3 = ("Python", "Java", "C#", "Php")
print(demet3.index("Java"))

# ekrana 1 yazdırır.
