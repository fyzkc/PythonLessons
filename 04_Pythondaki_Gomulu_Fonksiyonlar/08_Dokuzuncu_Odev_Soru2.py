"""
Problem 2
Elinizden her bir elemanı 3'lü bir demet olan bir liste olsun.

     [(3,4,5),(6,8,10),(3,10,7)]

Şimdi kenar uzunluklarına göre bu kenarların bir üçgen olup olmadığını dönen bir fonksiyon yazın 
ve sadece üçgen belirten kenarları bulunduran listeyi ekrana yazdırın.

     [(3, 4, 5), (6, 8, 10)]

*** Not: filter() fonksiyonunu kullanmaya çalışın. ***
"""

liste=[(3,4,5),(6,8,10),(3,10,7)]

def ucgen(demet):
    if((demet[0]+demet[1])>demet[2] and (demet[1]+demet[2])>demet[0] and (demet[0] + demet[2]) > demet[1]):
        return True
    else:
        return False
    
print(list(filter(ucgen,liste)))

#------------------------------------------------------------

#  ÇÖZÜM :

#------------------------------------------------------------

print("------------------------------------------------")

def üçgen_mi(demet):
    
    if (abs(demet[0]+demet[1]) > demet[2] and abs(demet[0]+demet[2]) > demet[1] and abs(demet[1]+demet[2]) > demet[0]):
        return True
    else:
        return False


liste = [(3,4,5),(6,8,10),(3,10,7)]

print(list(filter(üçgen_mi,liste)))

#ÇÖZÜM NOT: Üçgen kenarları toplamının mutlak değeri alınması gerektiği için abs fonksiyonu ile toplanması gerekir.
