"""

Dosya Açmak: open() fonksiyonu:

Bir dosyayı açmak için open() fonksiyonu kullanılır.

open(dosya_adi,dosya_erisme_kipi)

dosya adı: açılacak dosyanın adı
dosya erişme kipi: dosyaya yazma mı yoksa dosyadan okuma mı yapılacağı

Dosyaları açmak ve yazmak için "w" kipi kullanılır.
Eğer öyle bir dosya yoksa dosyayı oluşturur, ancak eğer öyle bir dosya
zaten varsa, o dosyanın üzerine yazar. Yani silip tekrar oluşturur.


"""

# file= open("bilgiler.txt","w")

#Bunu yazdığımız zaman bilgiler.txt adlı bir dosya oluşturulur.

#İşimiz bittikten sonra dosyayı kapatmazsak dosya arka planda gereksiz veri harcayabilir (çok büyük dosyalar için).
#O yüzden her zaman işimiz bittikten sonra dosyanın kapatılması gerekir.

# file.close()

#Eğer dosyayı bulunduğumuz klasörde değil de başka bir klasörde oluşturmak istersek
#oluşturulmasını istediğimiz klasörün yolunu yazmamız gerekir.

file= open("C:/Users/Feyza/Desktop/Python Dersleri/3-Dosya Islemleri/bilgiler.txt","w",encoding="utf-8")

#Dosya içerisine bir şeyler yazmak istersek:

file.write("Feyza Koç")

#Ancak bu şekilde içerisinde Türkçe karakter barındıran ifadeleri yazdığımızda
#Türkçe karakterler düzgün görüntülenmeyecektir.
#Bunun için ekstra bir parametre eklenmesi gerekiyor.

#encoding="utf-8" eklediğimizde sorun çıkmayacaktır.

file.close()


#Eğer dosya içerisindeki bilgileri silmeden dosya üzerine bilgi eklemek istersek append anlamına gelen
# "a" kipini kullanırız.

# "a" kipi ile eğer dosya yoksa oluşturulur, dosya varsa da içerisindeki bilgiler silinmeden üzerine yazma yapar.

file= open("C:/Users/Feyza/Desktop/Python Dersleri/3-Dosya Islemleri/bilgiler.txt","a",encoding="utf-8")
file.write("\nFeyza koç")

file.close()