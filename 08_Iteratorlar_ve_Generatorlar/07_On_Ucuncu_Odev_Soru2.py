"""
1'den 1000'e kadar olan sayılardan asal sayıları üreten generator bir fonksiyon yazın.
"""

def asalSayilar():
    asalMi=bool
    for i in range(1,1001):
        if(i==1):
            continue
        elif(i==2):
            yield i
        else:
            for j in range(2,i):
                if(i%j==0):
                    asalMi=False
                    break
                else:
                    asalMi=True
            if(asalMi==True):
                yield i


for i in asalSayilar():
    print(i)

