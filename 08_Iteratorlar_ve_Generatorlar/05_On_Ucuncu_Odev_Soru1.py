"""
"Kareler" isminde bir tane sınıf tanımlayın ve bu sınıfı iterable bir sınıf yapmaya çalışın. 
Bu sınıfın init fonksiyonu maksimum isimli bir tane parametre alsın ve her next işleminde 
ekrana üzerinde bulunduğunuz sayının karesi yazdırılsın. 
StopIteration hatası ekrana maksimum sayıyı geçtiğiniz zaman fırlatılsın.
"""

class Kareler():
    def __init__(self,maks):
        self.maks=maks
        self.sayi=0
    def __iter__(self):
        return self
    def __next__(self):
        if(self.sayi<=self.maks):
            kare= self.sayi ** 2
            self.sayi +=1
            return kare
        else:
            self.sayi=0
            raise StopIteration

kare= Kareler(5)
iterator= iter(kare)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
#print(next(iterator))

# 0
# 1
# 4
# 9
# 16
# 25
# Traceback (most recent call last):
#   File "c:\Users\Feyza\Desktop\Python Dersleri\8-Iteratorlar ve Generatorlar\5-On Uçüncü Odev Soru1.py", line 31, in <module>
#     print(next(iterator))
#           ^^^^^^^^^^^^^^
#   File "c:\Users\Feyza\Desktop\Python Dersleri\8-Iteratorlar ve Generatorlar\5-On Uçüncü Odev Soru1.py", line 20, in __next__
#     self.kuvvet
# AttributeError: 'Kareler' object has no attribute 'kuvvet'


for i in kare:
    print(i)