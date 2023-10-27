"""

Proje 2
--------------------------------
Bu projede ise 4 tane sınıfı oluşturun.

Hayvan Sınıfı ------> Bütün hayvanların ortak özelliklerinin toplandığı sınıf olacak.

Köpek Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa köpeklere ait ek özellikler ve metodlar ekleyin.

Kuş Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa kuşlara ait ek özellikler ve metodlar ekleyin.

At Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa atlara ait ek özellikler ve metodlar ekleyin.


"""

#Şube: Omurgalılar ve Omurgasızlar
#Sınıf: Omurgalılar: balıklar, amfibiler, sürüngenler, kuşlar ve memeliler,
#       Omurgasızlar: süngerler, sölenterler, solucanlar, yumuşakçalar, eklem bacaklılar ve derisi dikenliler 
#Aile: Köpekgiller, kedigiller vb.
#Cins: Köpekgiller içinde Köpek, Kurt, Tilki ve Çakal
#Tür: Canis türleri; Çizgili çakal (Canis adustus), Altın çakal (Canis aureus), Kır kurdu (Canis latrans), Kurt (Canis lupus) gibi.

class Hayvan():
    def __init__(self,sube,sinif,aile,cins,tur,alem="Hayvan"):
        self.alem=alem
        self.sube=sube
        self.sinif=sinif
        self.aile=aile
        self.cins=cins
        self.tur=tur


class Kopek(Hayvan):
    def __init__(self,tuyRenk, ceneGucu, kilo, yirticiMi, tur, alem="Hayvan", sube="Omurgalılar", sinif="Memeliler", aile="Köpekgiller", cins="Köpek"):
        super().__init__(sube, sinif, aile, cins, tur, alem)
        self.tuyRenk=tuyRenk
        self.ceneGucu=ceneGucu
        self.kilo=kilo
        self.yirticiMi=yirticiMi
    
    def BilgileriGoster(self):
        print(self.tur,"Özellikleri\n")
        print("Alem: {}\nŞube: {}\nSınıf: {}\nAile: {}\nCins: {}\nTür: {}\nTüy Rengi: {}\nÇene Gücü: {}\nKilo: {}\nYırtıcılık: {}".format(self.alem,self.sube,self.sinif,self.aile,self.cins,self.tur,self.tuyRenk,self.ceneGucu,self.kilo,self.yirticiMi))

class Kus(Hayvan):
    def __init__(self, yirticiMi, aile, cins, tur, alem="Hayvan", sube = "Omurgalılar", sinif="Kuşlar"):
        super().__init__(sube, sinif, aile, cins, tur, alem)
        self.yirticiMi=yirticiMi

    def BilgileriGoster(self):
        print(self.tur,"Özellikleri\n")
        print("Alem: {}\nŞube: {}\nSınıf: {}\nAile: {}\nCins: {}\nTür: {}\nYırtıcılık: {}".format(self.alem,self.sube,self.sinif,self.aile,self.cins,self.tur,self.yirticiMi))

class At(Hayvan):
    def __init__(self, tuyRenk, kosmaHizi, tur, alem="Hayvan", sube="Omurgalılar", sinif="Memeliler", aile="Atgiller", cins="At"):
        super().__init__(sube, sinif, aile, cins, tur, alem)
        self.tuyRenk=tuyRenk
        self.kosmaHizi=kosmaHizi
    
    def BilgileriGoster(self):
        print(self.tur,"Özellikleri\n")
        print("Alem: {}\nŞube: {}\nSınıf: {}\nAile: {}\nCins: {}\nTür: {}\nYırtıcılık: {}".format(self.alem,self.sube,self.sinif,self.aile,self.cins,self.tur,self.tuyRenk,self.kosmaHizi))


almanCobanKopegi= Kopek("Kahverengi",238,35,"Yırtıcı değil","Alman Çoban Köpeği")
almanCobanKopegi.BilgileriGoster()


        


