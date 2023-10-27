# list comprehension kullanmadan bir listedeki elemanları başka bir listeye atalım:

liste1 = [1, 2, 3, 4, 5]
liste2 = list()

for i in liste1:
    liste2.append(i)
print(liste2)

# bu şekilde bir listedeki elemanları başka bir listeye atabiliriz.

# LIST COMPREHENSION

liste3 = [1, 2, 3, 4, 5]
liste4 = [i for i in liste3]

# iç içe listelerde kullanım:

# önce list comprehension olmadan yapalım:

liste = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15]]
liste_ = list()
for i in liste:
    for x in i:
        liste_.append(x)

# list comprehension ile yapalım:

liste = [[1, 2, 3], [4, 5, 6, 7, 8, ], [9, 10, 11, 12, 13, 14, 15]]

liste_ = [x for i in liste for x in i]
