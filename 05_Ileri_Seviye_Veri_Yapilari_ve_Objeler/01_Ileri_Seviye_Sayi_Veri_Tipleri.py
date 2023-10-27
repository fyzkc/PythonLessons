"""
Bazen programlama yaparken, sayılarımızı 10'luk taban haricinde 
2'lik ve 16'lık olarak göstermek ve kullanmak isteyebiliriz.

Bunun için python'daki bin ve hex fonksiyonlarını kullanırız.

"""

#bin() fonksiyonu: 10'luk tabandaki bir sayının 2'lik tabanda gösterilmesini sağlar.

print(bin(4))
# Ekran çıktısı: 0b100


#hex() fonksiyonu: 10'luk tabandaki bir sayının 16'lım tabanda gösterilmesini sağlar.

print(hex(28))
# Ekran çıktısı: 0x1c

#Sayılar üzerinde uygulanabilen fonksiyonlar:

#abs() fonksiyonu: sayının mutlak değerini alır.

#round(): sayıları alta veya üste yuvarlar.

print(round(4.8))
print(round(4.5))
print(round(4.2))

print(round(3.2229,3)) 
#3 parametresi ondalıklı sayının virgülden sonraki ilk üç basamağı yuvarlamamızı söyler.
#Ekran çıktısı: 3.223
#en sonda 9 sayısı olduğu için 3. basamak 3'e yuvarlandı.

print(round(3.2224,3)) 
#Ekran çıktısı: 3.222
#en sonda 4 sayısı olduğu için 3. basamak 2'ye yuvarlandı.

#max() ve min() fonksiyonları: 
# max fonksiyonu en büyük sayıyı döndürür;
# min fonksiyonu en küçük sayıyı döndürür.

#sum() fonksiyonu: sayıların toplamını döndürür.
#ancak sayıların liste veya demet veritiplerinden biri şeklinde gönderilmesi gerekir.

#pow(): üs alma işlemi yapar

print(pow(2,4))
#2^4 işlemi yapar.

#NOT: Bu işlemi 2**4 şeklinde de yapabiliriz.