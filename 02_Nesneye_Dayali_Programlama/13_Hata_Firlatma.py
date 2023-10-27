"""
Bazen kendi özel hata mesajlarımızı tanımlamamız gerekebilir.
Bunun için raise anahtar kelimesini kullanmamız gerekir.
"""

# raise HataAdı(Hata mesajı)

def tersCevir(s):
    if(type(s)!=str):
        raise ValueError("Girdiğiniz ifade metinsel değil!")
    else:
        return s[::-1]

try:
    print(tersCevir(12)) #bu fonksiyonda zaten Value Error hatasını gönderdiğimiz için direkt ValueError except bloğuna girecektir.
except ValueError:
    print("Hata!")


