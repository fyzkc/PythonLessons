# Sözlükler içerisindeki her bir eleman indeks ile değil, anahtar(key) ve değer(value) olarak tutulur.

# örneğin, ingilizce türkçe çeviri bir sözlük oluşturduğumuzu varsayalım. anahtar(key) olarak "freedom" değerini verip değer(value) olarak "özgürlük" değerini alabiliriz.

# SÖZLÜK OLUŞTURMA

sozluk1 = {"bir": 1, "iki": 2, "üç": 3}

# boş sözlük:

sozluk2 = {}  # veya
sozluk2 = dict()

# SÖZLÜK DEĞERLERİNE ERİŞME

# sözlük değerlerine ulaşmak için indeksleri değil, anahtarları kullanırız.

sozluk1["bir"]

# bu şekilde 1 değerine erişebiliriz.

# SÖZLÜĞE ELEMAN EKLEME

sozluk1["beş"] = 5

# bu şekilde eleman eklenebilir. eklenen eleman en başa eklenir ve sözlükler sıralı değildir.

# elemanların değerlerini güncellemek istediğimizde, eleman eklemede yaptığımız gibi yapabiliriz.

sozluk1["beş"] = 10

# bu şekilde sözlük üzerindeki beş anahtar kelimesinin değeri artık 10 olur.

sozluk1["beş"] += 1

# bu şekilde de beş anahtar kelimesinin değerini 1 arttırabiliriz.

# İÇ İÇE SÖZLÜKLER

a = {"sayilar": {"bir": 1, "iki": 2, "üç": 3}, "meyveler": {
    "kiraz": "yaz", "portakal": "kış", "erik": "yaz"}}

# bu şekilde iç içe sözlükler kullanılabilir.

# SÖZLÜK METOTLARI

# keys() metodu, sözlük içerisindeki anahtarları yazdırır.

# values() metodu, sözlük içerisindeki değerleri yazdırır.

# items() metodu, sözlük içerisindeki anahtar ve değerleri tuple'lara dönüştürmeyi sağlar.

# dict_items([('bir',1),('iki',2),('üç',3),('dört',4)])

# dönüştürüldükten sonra tuple olarak bu hali alır.
