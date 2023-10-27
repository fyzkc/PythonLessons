def Not(satir):
    satir= satir[:-1] #son karakter haricindeki yazdırması için. Son karakter de \n olduğu için fazladan boşluk olmasın diye.
    liste=satir.split(",")
    isim=liste[0]
    not1=int(liste[1])
    not2=int(liste[2])
    not3=int(liste[3])

    ortalama=(not1*(3/10)) + (not2*(3/10))+ (not3*(4/10))

    if(ortalama>=90):
        harfNotu="AA"
    elif(ortalama>=85):
        harfNotu="BA"
    elif(ortalama>=80):
        harfNotu="BB"
    elif(ortalama>=75):
        harfNotu="CB"
    elif(ortalama>=70):
        harfNotu="CC"
    elif(ortalama>=65):
        harfNotu="DC"
    elif(ortalama>=60):
        harfNotu="DD"
    else:
        harfNotu="FF"
    
    return isim + "=" + harfNotu + "\n"

with open("C:/Users/Feyza/Desktop/Python Dersleri/3-Dosya Islemleri/Notlar.txt","r",encoding="utf-8") as file:
    eklenecekler=list()
    for i in file:
        eklenecekler.append(Not(i))
    print(eklenecekler)

with open("C:/Users/Feyza/Desktop/Python Dersleri/3-Dosya Islemleri/Ortalamalar.txt","w",encoding="utf-8") as file2:
    for i in eklenecekler:
        file2.write(i)
