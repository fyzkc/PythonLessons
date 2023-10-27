# SEP PARAMETRESİ

# sep parametresi, ard arda birden fazla string ifadeyi yazdırmak istediğimizde, yazdırılacak olan her ifadenin arasında ne olacağını belirlemek için kullanılır.

# ÖRNEK:

print(35, 34, 36, 56)

# Böyle yazdığımızda ekran çıktısı olarak sayıların arasında boşluk olacak şekilde yazar.

# 35 34 36 56 şeklinde

print(35, 34, 36, 56, sep="/")

# bu şekilde bir kullanım yaparsak ise sayıların arasında / işareti olacak şekilde ekrana yazdırır.

# YILDIZ İŞARETİ

# yazdıracağımız string değerin başına yıldız işareti koyduğumuzda, string ifadenin her bir karakterinin arasında boşluk olur.

# ÖRNEK:

print(*"Python")

# P y t h o n

# bu şekilde bir çıktı alırız.

# yıldız işareti kullanırken de sep parametresini kullanabiliriz.

print(*"TBMM", sep=".")

# T.B.M.M şeklinde yazdırır.

# FORMAT FONKSİYONU

# ÖRNEK:

a = 3
b = 4
print("{} + {} = {}".format(a, b, a+b))

# 3 + 4 = 7 çıktısını yazdırır.

# eğer kullanacağımız değerlerin sırasını değiştirmek istersek de şu şekilde bir kullanım yaparız:

print("{1} {0} {2}".format("Feyza", "1", "Koç"))

# 1 Feyza Koç

# ondalıklı sayılarda virgülden sonra kaç basamağın alınacağını belirlemek için de şu şekilde bir kullanım yaparız:

print("{:.2f} {:.3f}".format(3.122445, 3.24545))

# 3.12 3.245  olarak yazdırır.
