"""
Datetime modülü zaman ve tarih işlemleri için kullanılan hazır bir modüldür.
"""

from datetime import datetime
#datetime modülü içerisindeki datetime sınıfını import ettik
import locale

print(datetime.now())
#2023-08-13 18:00:33.370230

#datetime.now() : şimdiki zamanı yıl, ay, gün, saat,dakika ve saniye cinsinden döndürür.

#sadece yılı veya ayı almak istersek:

print(datetime.now().year)
#2023

print(datetime.now().month)
#8

print(datetime.now().microsecond)
#518324

print(datetime.now().hour)
#18

#Tarih ve saat bilgisini daha iyi bir şekilde ekrana yazdırmak için:
#datetime.ctime() fonksiyonu kullanılır.

print(datetime.ctime(datetime.now()))
#Sun Aug 13 18:05:18 2023

#strftime(): datetime objesi içerisinden ay, yıl, gün vb bilgileri
#almamızı sağlar.

#datetime.now() objesini bir değişkene atayarak da kullanabiliriz.

simdi=datetime.now()

#yıl bilgisi için %Y:
print(datetime.strftime(simdi,"%Y"))
#2023

#ay ismi için %B:
print(datetime.strftime(simdi,"%B"))
#August

#gün ismi için %A:
print(datetime.strftime(simdi,"%A"))
#Sunday

#saat bilgisi için %X:
print(datetime.strftime(simdi,"%X"))
#18:11:17

#o günün tarihi için için %D:
print(datetime.strftime(simdi,"%D"))
#08/13/23

#tabi bu parametreleri aynı anda vererek yan yana birden fazla bilgiyi de yazdırabiliriz:

print(datetime.strftime(simdi,"%B %Y"))
#August 2023

print(datetime.strftime(simdi,"%A %B %Y"))
#Sunday August 2023

#Ancak bu isimleri Türkçe olarak da gösterebiliriz.
#Bunun için şu anki konumumuzun Türkçe konuşulan bir yer olduğunu belirtmemiz gerekir.
#bunun için locale isimli bir modülü import etmemiz gerekir öncelikle.
#Daha sonra yerimizin Türkiye olduğunu belirtmemiz lazım:

locale.setlocale(locale.LC_ALL,"")
#Burada tırnak içine herhangi bir değer yazmadığımızda zaten mevcut olarak bulunduğumuz
#yeri set eder ve yazıların türkçe görünmesini sağlar.

print(datetime.strftime(simdi,"%A %B %Y"))
#Pazar Ağustos 2023

#tırnak içine ülkelerin kodlarını yazarak farklı dillerde de yazdırabiliriz.

#timestamp() ve fromtimestamp():
#Şu anki zamanı saniye cinsinden bulmak için timestamp() fonksiyonu kullanılır.
#Saniye cinsinden verilen zamanı da datetime objesine çevirmek için fromtimestamp() fonksiyonu kullanılır.

print(simdi)
#2023-08-13 18:25:01.432362

#bu değeri saniye cinsine çevirmek istersek:
saniye=datetime.timestamp(simdi)
print(saniye)
#1691940378.366494

zaman=datetime.fromtimestamp(saniye)
print(zaman)
#2023-08-13 18:26:53.233712

#0. saniyenin hangi tarihe karşılık geldiğine bir bakalım:
saniye=datetime.fromtimestamp(0)
print(saniye)
#1970-01-01 03:00:00

#Bunun sebebi şudur:
#Bilgisayarcılar, zamanın başlangıcını bu tarih olarak kabul etmişler.
#Ve o günden bu yana bilgisayarlarımız aslında saniyeleri sayar.
#Ve saniyelerin, bu tarihe göre karşılığını bulup o şekilde bugünün tarihini gösterir.
#Bu tarihe "Epoch time" denir.


#İki tarih arasındaki farkı bulma:

#datetime objelerimizi yalnızca datetime.now() diyerek değil
#kendimiz belirli tarih ve saat değerleri vererek de oluşturabiliriz.

tarih=datetime(2001,2,9)
simdi=datetime.now()
#iki tarih arasındaki farkı ölçmek için:

print(simdi-tarih)
#8220 days, 18:38:16.105689 
#aradaki zaman farkı bu şekilde bulunur.



#NOT: Diğer bütün gösterimler için https://docs.python.org/2/library/time.html buraya bakılabilir.

