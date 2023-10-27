import sqlite3

con=sqlite3.connect("Kütüphane.db")
cursor=con.cursor()

def tumVeriler():
    cursor.execute("SELECT * FROM Kitaplık")
    liste= cursor.fetchall() #veritabanından dönecek olan veriler fetchall fonksiyonu ile görüntülenir.
    #bu fonksiyon veritabanı verilerini bir liste şeklinde döndürür. O yüzden bir liste değişkenine eşitledik.
    #diğer sorgularda olduğu gibi veritabanı üzerinde herhangi bir işlem yapmadığımız (veri ekleme, tablo oluşturma vb.) için
    #commit() fonksiyonunu kullanmamız gerekmiyor.

    for i in liste:
        print(i)

print("Tüm Veriler:")
tumVeriler()
print("---------------------------")

def isimVeYazar():
    cursor.execute("SELECT İsim, Yazar FROM Kitaplık")
    liste= cursor.fetchall()

    for i in liste:
        print(i)

print("İsim ve Yazar Bilgileri:")
isimVeYazar()
print("---------------------------")

def YayinevleriniGoster(yayinevi):
    cursor.execute("SELECT * FROM Kitaplık WHERE Yayınevi = ?",(yayinevi,))
    liste= cursor.fetchall()

    for i in liste:
        print(i)

print("Yayınevine Göre Bilgiler:")
YayinevleriniGoster("Everest")
print("---------------------------")
con.close()