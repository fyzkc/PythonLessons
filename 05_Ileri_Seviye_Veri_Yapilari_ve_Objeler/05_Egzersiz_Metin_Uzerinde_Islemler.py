class Dosya():
    def __init__(self):
        with open("C:/Users/Feyza/Desktop/Python Dersleri/5-Ileri Seviye Veri Yapıları ve Objeler/metin.txt","r",encoding="utf-8") as file: #metin dosyasını açtık
            dosyaIcerigi=file.read() #metin dosyasının içeriğini dosyaIcerigi değişkenine atadık.
            kelimeler=dosyaIcerigi.split() #metnin tüm kelimelerini ayırdık.
            self.sadeceKelimeler=list()

            for i in kelimeler:
                i=i.strip("\n") #kelimelerin başında ve sonunda bulunan \n karakterlerini sildik.
                i=i.strip(" ") #kelimelerin başında ve sonunda bulunan boşluk karakterlerini sildik.
                i=i.strip(".") #kelimelerin başında ve sonunda bulunan nokta karakterlerini sildik.
                i=i.strip(",") #kelimelerin başında ve sonunda bulunan virgül karakterlerini sildik.
                self.sadeceKelimeler.append(i) #sadeleşmiş olan kelimeleri sadeceKelimeler listemize attık.

            # print(self.sadeceKelimeler)

    def tumKelimeler(self):
        kelimelerKumesi=set() #her bir kelimeyi bir kümeye atmak için kelimelerKumesi adında bir küme oluşturduk.
        for i in self.sadeceKelimeler:
            kelimelerKumesi.add(i)

        print("Tüm kelimeler: ",kelimelerKumesi)

    def kelimeFrekansi(self): #bir kelimenin kaç kere geçtiğini bu fonksiyonla bulalım.
        #sözcüklerin kaç kere geçtiğini tutabilmek için bir sözlük yapısı kullanalım.
        #sözlüğün içerisindeki anahtarlar kelimeler, o anahtarların değerleri ise o kelimelerin kaç kere geçtiği olsun.

        sozluk=dict()
        for i in self.sadeceKelimeler:
            if(i in sozluk): #kelimenin sözlük içerisinde olup olmadığını kontrol edelim.
                sozluk[i]+=1 #eğer kelime sözlük içerisinde varsa, kelimenin değerini bir arttıracağız.
            else:
                sozluk[i]=1 #eğer kelime daha önce sözlükte yoksa, kelimeyi szölüğe anahtar olarak ekleyip, değerini de 1 olarak başlatacağız.
    
        for kelime,sayi in sozluk.items():
            print("{} kelimesi metin içerisinde {} defa geçiyor".format(kelime,sayi))


dosya=Dosya()
dosya.tumKelimeler()
dosya.kelimeFrekansi()