import sqlite3
import time

class Kitap(): #Kitap classı
    def __init__(self,isim,yazar,yayinevi,tur,baski):
        self.isim= isim
        self.yazar=yazar
        self.yayinevi=yayinevi
        self.tur=tur
        self.baski=baski

    #kitap classı içerisinde, print fonksiyonu çağırıldığında gerçekleşecek olan fonksiyon:
    def __str__(self):
        return "Kitap İsmi: {}\nYazar: {}\nYayınevi: {}\nTür: {}\nBaskı: {}\n".format(self.isim,self.yazar,self.yayinevi,self.tur,self.baski)
    

class Kutuphane():
    def __init__(self):
        self.baglantiOlustur()

    def baglantiOlustur(self):
        self.baglanti= sqlite3.connect("KütüphaneProjesi.db")
        #KütüphaneProjesi isimli veritabanına bağlanıyoruz. Öyle bir veritabanı yoksa da oluşturuyor.
        self.cursor = self.baglanti.cursor()
        
        sorgu= "CREATE TABLE IF NOT EXISTS Kitaplar (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Tür TEXT, Baskı INT)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()

    def baglantiKapat(self):
        self.baglanti.close()

    def kitaplariGoster(self):
        sorgu = "SELECT * FROM Kitaplar"
        self.cursor.execute(sorgu)
        kitaplar=self.cursor.fetchall() #bu kod ile veriler liste içerisinde demet halinde döndürülür ve kitap değişkenine atanır.

        if(len(kitaplar)==0):
            print("Kütüphanede hiç kitap yok.")
        else:
            for i in kitaplar:
                #kitap isimli Kitap sınıfından bir nesne oluşturduk.
                #oluştururken de init fonksiyonunun parametrelerini,
                #kitaplar listesi içerisindeki veriler olarak gönderdik.
                #burada i elemanı kitaplar listesi içerisindeki her bir demet olarak bulunuyor.
                #demetler içerisinde de kitapların adı, yazarı gibi bilgiler bulunuyor.
                #yani her bir demetin 0., 1., 2., 3. ve 4. elemanları bu özellikleri ifade ediyor.
                kitap=Kitap(i[0],i[1],i[2],i[3],i[4])
                #bu şekilde kitap nesnesini oluşturduk ve içerisinde kitapların bilgileri oluştu.
                print(kitap)
                #yukarıda str fonksiyonunu kendimiz tanımlamıştık ve kitapların bilgilerini yazdırmak için kullanmıştık.
                #bu sayede print() fonksiyonunu direkt olarak kullanarak bu bilgileri ekrana yazdırabileceğiz.

    def kitapSorgula(self,isim):
        sorgu= "SELECT * FROM Kitaplar WHERE İsim= ?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar= self.cursor.fetchall()
        #ismi istenen isim olan kitapların listesini getirdik ve kitaplar listesine attık. 
        #Her bir kitap demet şeklinde listenin içinde atıldı.
        if(len(kitaplar)==0):
            print("Böyle bir kitap bulunmuyor.")
        else:
            #kitap nesnesini oluştururken, ilk parametreyi kitaplar listesinin ilk demetinin ilk elemanı olan isim verisini verdik.
            #diğer elemanlar da diğer parametreler için.
            #her seferinde 0. indis üzerinden işlem yapmamızın sebebi listemizin tek elemanlı bir liste olacak olması.
            #Çünkü aynı isimden birden fazla kitap olamaz.
            kitap=Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])
            print(kitap)
    
    def kitapEkle(self,kitap): #parametre olarak bir kitap nesnesi göndereceğiz.
        sorgu= "INSERT INTO Kitaplar VALUES (?,?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayinevi,kitap.tur,kitap.baski))
        self.baglanti.commit()

    def kitapSil(self,isim):
        sorgu = "DELETE FROM Kitaplar WHERE İsim = ?"
        self.cursor.execute(sorgu,(isim,))
        self.baglanti.commit()

    def baskiYukselt(self,isim):
        sorgu = "SELECT * FROM Kitaplar WHERE İsim = ?"
        self.cursor.execute(sorgu,(isim,))
        kitap= self.cursor.fetchall()
        if(len(kitap)==0):
            return False
        else:
            baski= kitap[0][4]
            baski +=1
            sorgu2 = "UPDATE Kitaplar SET Baskı = ? WHERE İsim= ?"
            self.cursor.execute(sorgu2,(baski,isim))
            self.baglanti.commit()
