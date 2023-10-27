#seek() ve write() fonksiyonları ile değişiklik:

# with open("C:/Users/Feyza/Desktop/Python Dersleri/3-Dosya Islemleri/bilgiler.txt","r+",encoding="utf-8") as file:
#     print(file.read())

# "r+" dosya kipi: Bu dosya kipi hem dosyadan okuma yapmayı, hem de dosyaya yazmayı sağlar.

#Yukarıdaki kod sonucunda file değişkeni dosyanın en sonunda olacaktır.
#Çünkü yukarıdan aşağıya doğru tüm dosyayı okur ve okuma işlemi bittiğinde de dosyanın en sonunda olacaktır.

# seek() fonksiyonu ile file değişkenini dosyanın farklı bir yerine götürelim ve yazma işlemi yapalım:

# with open("C:/Users/Feyza/Desktop/Python Dersleri/3-Dosya Islemleri/bilgiler.txt","r+",encoding="utf-8") as file:
#     file.seek(10)
#     file.write("Deneme")

# with open("C:/Users/Feyza/Desktop/Python Dersleri/3-Dosya Islemleri/bilgiler.txt","r+",encoding="utf-8") as file:
#     print(file.read())

#Feyza KoçDenemea koç
#pyhton, java, c, c#

#çıktısını alırız.

#Dosyanın sonunda değişiklik yapma:

#"a" kipiyle açtığımız bir dosyada imleç dosyanın sonunda olacağı için write() ile yazdığımızda
#direkt olarak dosyanın sonuna yazma işlemi yapabiliriz.

# with open("C:/Users/Feyza/Desktop/Python Dersleri/3-Dosya Islemleri/bilgiler.txt","a",encoding="utf-8") as file:
#     file.write("Muhammed Sert\n")

# with open("C:/Users/Feyza/Desktop/Python Dersleri/3-Dosya Islemleri/bilgiler.txt","r+",encoding="utf-8") as file:
#     print(file.read())

#Bu şekilde eklediğimiz ifadenin dosyanın en sonunda olduğunu görebiliriz.

#Dosyanın başında değişiklik yapma:

# with open("C:/Users/Feyza/Desktop/Python Dersleri/3-Dosya Islemleri/bilgiler.txt","r+",encoding="utf-8") as file:
#     icerik=file.read() #içeriğin tamamını aldık.
#     icerik= "Muhammed Sert\n" + icerik #İçeriği bu şekilde güncelledik
#     file.seek(0) #dosyanın en başına gittik
#     file.write(icerik) #güncellediğimiz içeriği yazdırma işlemini yaptık.


#Dosyanın ortasında değişiklik yapma:

#readlines() metodu ile dosya içeriğini liste haline çevirip,
#bu liste üzerinden insert metodu ile dosyanın istediğimiz yerine ekleme yapabiliriz.

# with open("C:/Users/Feyza/Desktop/Python Dersleri/3-Dosya Islemleri/bilgiler.txt","r+",encoding="utf-8") as file:
#     liste= file.readlines() #dosya içeriğini listeye attık
#     liste.insert(3,"Feyza\n") #listenin 3. indexine Feyza değerini ekledik.
#     file.seek(0) #dosyanın en başına geldik
#     for i in liste: #dosyanın en başından sırasıyla liste içerisindeki elemanları tek tek dosya üzerine yazma işlemi yaptık.
#         file.write(i)
    
with open("C:/Users/Feyza/Desktop/Python Dersleri/3-Dosya Islemleri/bilgiler.txt","r+",encoding="utf-8") as file:
    print(file.read())

# for i in liste:
#         file.write(i)
#Bu ifade yerine şöyle bir şey yapılabilirdi:

with open("C:/Users/Feyza/Desktop/Python Dersleri/3-Dosya Islemleri/bilgiler.txt","r+",encoding="utf-8") as file:
    liste= file.readlines() #dosya içeriğini listeye attık
    liste.insert(3,"Koç\n") #listenin 3. indexine Feyza değerini ekledik.
    file.seek(0) #dosyanın en başına geldik
    file.writelines(liste)

#Bu şekilde writelines ile her bir satır tek tek dosyaya yazılır.


