import sqlite3

con= sqlite3.connect("Kütüphane.db")
cursor=con.cursor()

def veriEkle():
    cursor.execute("INSERT INTO Kitaplık VALUES('İstanbul Hatırası', 'Ahmet Ümit', 'Everest', 561)")
    con.commit()

#Kullanıcıdan aldığımız verileri girmek için:

def veriEkle2(isim,yazar,yayinevi,sayfaSayisi):
    cursor.execute("INSERT INTO Kitaplık VALUES(?,?,?,?)",(isim,yazar,yayinevi,sayfaSayisi))
    con.commit()


isim=input("İsim: ")
yazar= input("Yazar: ")
yayinevi = input("Yayınevi: ")
sayfaSayisi= int(input("Sayfa Sayısı: "))

#veriEkle2(isim,yazar,yayinevi,sayfaSayisi)
#veriEkle()
con.close()