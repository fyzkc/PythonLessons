"""
PROBLEM1: Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın:

Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

BKİ 18.5'un altındaysa -------> Zayıf

BKİ 18.5 ile 25 arasındaysa ------> Normal

BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

BKİ 30'un üstündeyse -------------> Obez

PROBLEM2: Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.

PROBLEM3: Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

Vize1 toplam notun %30'una etki edecek.

Vize2 toplam notun %30'una etki edecek.

Final toplam notun %40'ına etki edecek.


Toplam Not >=  90 -----> AA

Toplam Not >=  85 -----> BA

Toplam Not >=  80 -----> BB

Toplam Not >=  75 -----> CB

Toplam Not >=  70 -----> CC

Toplam Not >=  65 -----> DC

Toplam Not >=  60 -----> DD

Toplam Not >=  55 -----> FD

Toplam Not <  55 -----> FF

PROBLEM4: Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.
NOT: Bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz.
"""

# PROBLEM1
# ---------------------------------------------------

boy = float(input("Boyunuzu girin(metre cinsinden): "))
kilo = float(input("Kilonuzu girin: "))
bki = kilo/(boy**2)
print("Beden kitle indeksiniz: {}".format(bki))

if(bki < 18.5):
    print("Zayıf")
elif(bki > 18.5 and bki < 25):
    print("Normal Kilo")
elif(bki > 25 and bki < 30):
    print("Fazla Kilolu")
else:
    print("Obez")


# PROBLEM2
# ---------------------------------------------------

sayi1 = int(input("Birinci sayı: "))
sayi2 = int(input("İkinci sayı: "))
sayi3 = int(input("Üçüncü sayı: "))

if(sayi1 > sayi2):
    if(sayi1 > sayi3):
        print("En büyük sayı: {}".format(sayi1))
    else:
        print("En büyük sayı: {}".format(sayi3))
elif(sayi3 > sayi2):
    print("En büyük sayı: {}".format(sayi3))
else:
    print("En büyük sayı: {}".format(sayi2))


# PROBLEM3
# ---------------------------------------------------

vize1 = int(input("Birinci vize notunuzu girin: "))
vize2 = int(input("İkinci vize notunuzu girin: "))
final = int(input("Final notunuzu girin: "))

toplam_not = (vize1*0.3) + (vize2*0.3) + (final*0.4)

if(toplam_not >= 90):
    print("AA")
elif(toplam_not >= 85):
    print("BA")
elif(toplam_not >= 80):
    print("BB")
elif(toplam_not >= 75):
    print("CB")
elif(toplam_not >= 70):
    print("CC")
elif(toplam_not >= 65):
    print("DC")
elif(toplam_not >= 60):
    print("DD")
elif(toplam_not >= 55):
    print("FD")
else:
    print("FF")


# PROBLEM4
# ---------------------------------------------------

tip = int(
    input("Tipiniz bulmak istediğiniz şekli yazın:\n1.Üçgen\n2.Dikdörtgen\n"))

if(tip == 2):
    kenar1 = int(input("Birinci kenar uzunluğunu girin: "))
    kenar2 = int(input("İkinci kenar uzunluğunu girin: "))
    kenar3 = int(input("Üçüncü kenar uzunluğunu girin: "))
    kenar4 = int(input("Dördüncü kenar uzunluğunu girin: "))
    if(kenar1 == kenar2 and kenar1 == kenar3 and kenar1 == kenar4):
        print("Bu bir kare")
    elif((kenar1 == kenar2 and kenar3 == kenar4) or (kenar1 == kenar3 and kenar2 == kenar4) or (kenar1 == kenar4 and kenar2 == kenar3)):
        print("Bu bir dikdörtgen")
    else:
        print("Bu bir dörtgen")
elif(tip == 1):
    birinci_kenar = int(input("Birinci kenar uzunluğunu girin: "))
    ikinci_kenar = int(input("İkinci kenar uzunluğunu girin: "))
    ucuncu_kenar = int(input("Üçüncü kenar uzunluğunu girin: "))
    if((birinci_kenar+ikinci_kenar) > ucuncu_kenar and (birinci_kenar+ucuncu_kenar) > ikinci_kenar and (ikinci_kenar+ucuncu_kenar) > birinci_kenar):
        if(birinci_kenar == ikinci_kenar and birinci_kenar == ucuncu_kenar):
            print("Eşkenar üçgen")
        elif(birinci_kenar == ikinci_kenar or birinci_kenar == ucuncu_kenar or ikinci_kenar == ucuncu_kenar):
            print("İkizkenar üçgen")
        else:
            print("Üçgen")
    else:
        print("Girdiğiniz değerler bir üçgen belirtmiyor.")

"""
problem4 ingilizce

shape = int(
    input("Write the shape that you want to find it's type:\n1.Triangle\n2.Quadrangle\n"))

if(shape == 2):
    edge1 = int(input("Enter the length of first edge: "))
    edge2 = int(input("Enter the length of second edge: "))
    egde3 = int(input("Enter the length of third edge: "))
    egde4 = int(input("Enter the length of forth edge: "))
    if(edge1 == edge2 and edge1 == egde3 and edge1 == egde4):
        print("This is a square")
    elif((edge1 == edge2 and egde3 == egde4) or (edge1 == egde3 and edge2 == egde4) or (edge1 == egde4 and edge2 == egde3)):
        print("This is a rectangle")
    else:
        print("This is a quadrangle")
elif(shape == 1):
    firstEdge = int(input("Enter the length of first edge: "))
    secondEdge = int(input("Enter the length of second edge: "))
    thirdEdge = int(input("Enter the length of third edge: "))
    if((firstEdge+secondEdge) > thirdEdge and (firstEdge+thirdEdge) > secondEdge and (secondEdge+thirdEdge) > firstEdge):
        if(firstEdge == secondEdge and firstEdge == thirdEdge):
            print("Equilateral Triangle")
        elif(firstEdge == secondEdge or firstEdge == thirdEdge or secondEdge == thirdEdge):
            print("Isosceles Triangle")
        else:
            print("Triangle")
    else:
        print("The values that you entered, can't make a triangle")




"""