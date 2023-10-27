# IN OPERATÖRÜ

# in operetörü, bir elemanın herhangi bir listede, demette veya stringte bulunup bulunmadığını kontrol eder ve true veya false döndürür.

5 in [1, 2, 3, 4]

# bunun sonucunda 5 bu liste içerisinde bulunmadığı için false döndürür.

2 in [1, 2, 3, 4]

# 2 sayısı bu listede bulunduğundan true döndürür.

"p" in "python"

# true değer döndürür.

# FOR DÖNGÜSÜ

liste = [1, 2, 3, 4, 5, 6, 7]

for eleman in liste:
    print(eleman)

"""
ekran çıktısı:
1
2
3
4
5
6
7
"""

kelime = "python"

for i in kelime:
    print(i)

"""
ekran çıktısı:
p
y
t
h
o
n
"""

# demetlerde de gezinebiliriz.

liste1 = [(1, 2), (3, 4), (5, 6), (7, 8)]

for (i, j) in liste1:
    print(i, j)

"""
ekran çıktısı:
1 2
3 4
5 6
7 8
"""
