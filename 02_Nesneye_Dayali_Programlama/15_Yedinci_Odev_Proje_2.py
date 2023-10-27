"""
Problem 2
Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın. 
Bu fonksiyon, eğer sayı çift ise *return* ile bu değeri dönsün. 
Ancak sayı tek sayı ise fonksiyon *raise* ile *ValueError* hatası fırlatsın. 

"""

def CiftMiTekMi(sayi):
    if(sayi%2==0):
        return sayi
    else:
        raise ValueError()
    
sayi= int(input("Bir sayı girin: "))
try:
    print(CiftMiTekMi(sayi))
except ValueError:
    print("Bu sayı tek sayıdır.")