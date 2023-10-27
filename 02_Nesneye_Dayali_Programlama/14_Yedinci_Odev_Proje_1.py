"""
Problem 1
Elinizde stringlerin bulunduğu bir liste bulunduğunu düşünün.

liste = ["345","sadas","324a","14","kemal"]

Bu listenin içindeki stringlerden içinde sadece rakam bulunanları ekrana yazdırın. 
Bunu yaparken try,except bloklarını kullanmayı unutmayın.
"""

liste= ["123","abc","12df","aaaa","23432f","209"]

def sayilar(i):
    if(i.isdigit()):
        print(i)
    else:
        raise ValueError()

for i in liste:
    try:
        sayilar(i)
    except ValueError:
        print("Bu ifade yalnızca sayılardan oluşmuyor.")
        
        
