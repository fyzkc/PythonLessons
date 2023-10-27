"""
Proje 2
"futbolcular.txt" şeklinde bir dosya oluşturun ve içine Galatasaray,Fenerbahçe ve Beşiktaşta oynayan futbolcuları rastgele yerleştirin. 
Bu dosyadan herbir takımın futbolcularını ayırarak "gs.txt" , "fb.txt", "bjk.txt" şeklinde 3 farklı dosyaya yazın.

"futbolcular.txt" dosyasının başlangıç hali şu şekilde olsun.

                Fernando Muslera,Galatasaray
                Atiba Hutchinson,Beşiktaş
                Simon Kjaer,Fenerbahçe
                           //
                           //
                           //
                           //
                           //

"""




def Satir(a):
    a=a[:-1]
    liste=a.split(",")
    isim=liste[0]
    takim=liste[1]

    return isim + takim

with open("C:/Users/Feyza/Desktop/Python Dersleri/3-Dosya Islemleri/futbolcular.txt","r",encoding="utf-8") as file:
    fenerbahce=list()
    besiktas=list()
    galatasaray=list()

    for i in file:
        if("Beşiktaş" in Satir(i)):
            besiktas.append(i)
        elif("Galatasaray" in Satir(i)):
            galatasaray.append(i)
        elif("Fenerbahçe" in Satir(i)):
            fenerbahce.append(i)

with open("C:/Users/Feyza/Desktop/Python Dersleri/3-Dosya Islemleri/Galatasaray.txt","w",encoding="utf-8") as file2:
    for i in galatasaray:
        file2.write(i)

with open("C:/Users/Feyza/Desktop/Python Dersleri/3-Dosya Islemleri/Beşiktaş.txt","w",encoding="utf-8") as file3:
    for i in besiktas:
        file3.write(i)

with open("C:/Users/Feyza/Desktop/Python Dersleri/3-Dosya Islemleri/Fenerbahçe.txt","w",encoding="utf-8") as file4:
    for i in fenerbahce:
        file4.write(i)