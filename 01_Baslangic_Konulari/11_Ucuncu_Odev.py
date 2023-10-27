"""
PROBLEM 1: Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)

PROBLEM 2: Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4

PROBLEM 3: 1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

*İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.*

PROBLEM 4: Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

*İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.*

PROBLEM 5: 1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi *continue* ile yapmaya çalışın.

PROBLEM 6: Buradaki problemin çözümünü derslerimizde özellikle öğrenmedik. Burada mantık yürüterek ve list comprehension kullanarak 1'den 100'e kadar olan sayılardan sadece çift sayıları bir listeye atmayı yapmayı çalışın.

Not: Programlamada her detayı öğrenemeyiz. Bunun için bazı yerlerde deneme yanılma yoluyla da öğrendiğimiz şeyler olur. Bu problemde deneme yanılma yoluyla list comprehension'ın koşullu durumlarla kullanımını öğreneceksiniz.

İpucu: Basit düşünmeye çalışın.
"""

# PROBLEM 1:

# sayi = int(input("Bir sayı giriniz: "))
# toplam = 0

# for i in range(1, sayi):
#     if(sayi % i == 0):
#         toplam += i

# if(toplam == sayi):
#     print("Bu bir mükemmel sayıdır.")
# else:
#     print("Bu bir mükemmel sayı değildir.")


# PROBLEM 2:

# sayi = int(input("bir sayı giriniz: ")) 
# sayi_ = sayi
# sayi2_ = sayi_
# basamak = 1

# while((int(sayi/10)) > 0):   
#     basamak += 1
#     sayi = int(sayi/10)     

# toplam = 0

# for i in range(0, basamak):
#     toplam += ((int(sayi_ % 10))**basamak)
#     sayi_ = int(sayi_/10)

# if(sayi2_ == toplam):
#     print("Girdiğiniz sayı bir Armstrong sayıdır.")
# else:
#     print("Girdiğiniz sayı bir Armstrong sayı değildir.")

# PROBLEM 3

# for i in range(1, 11):
#     for j in range(1, 11):
#         print("{}x{} = {}".format(i, j, i*j))
#     print()

# PROBLEM 4

# toplam = 0
# while(True):
#     sayi = input(
#         "Bir sayı giriniz veya programdan çıkmak ve girdiğiniz sayıların toplamını görmek istiyorsanız 'Q' ye basınız: ")
#     if(sayi == 'Q' or sayi == 'q'):
#         print("Programdan çıkılıyor.")
#         break
#     else:
#         toplam += int(sayi)

# print("Girdğiniz sayıların toplamı: {}".format(toplam))

# PROBLEM 5

# for i in range(1, 101):
#     if (i % 3 != 0):
#         continue
#     else:
#         print(i)

# PROBLEM 6

# sayilar = range(1, 101)
# ciftSayilar = [x for x in sayilar if x % 2 == 0]
# for a in ciftSayilar:
#     print(a)
