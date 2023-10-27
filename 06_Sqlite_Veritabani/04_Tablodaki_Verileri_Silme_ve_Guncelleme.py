import sqlite3

#Verileri Güncelleme:

con= sqlite3.connect("Kütüphane.db")
cursor=con.cursor()

def verileriGuncelle(eskiYayinevi,yeniYaninevi):
    cursor.execute("UPDATE Kitaplık SET Yayınevi = ? WHERE Yayınevi = ?",(yeniYaninevi,eskiYayinevi))
    con.commit()


verileriGuncelle("Doğan Kitap","Everest")


#Verileri Silme:

def verileriSil(yazar):
    cursor.execute("DELETE FROM Kitaplık WHERE Yazar= ?",(yazar,))
    con.commit()

verileriSil("Ahmet Ümit")


con.close()