"""
Python'da her bi dosya bir Modül'dür ve her bir modül içinde fonksiyonlar, sınıflar ve objeler barındırır.

Modülleri programlarımıza dahil ederek içerisindeki fonksiyonları, sınıfları veya objeleri kullanabiliriz.

Modüller olmasaydı, programımızdaki her bir fonksiyonu ve her bir sınıfı kendimiz yazmak zorunda kalacaktır.

Python geliştiricileri tarafından yazılmış bir çok hazır modül bulunmaktadır.

"""

#MODÜLLERİN PROGRAMA DAHİL EDİLMESİ

# import modül_adı 
#bu şekilde programımıza kullanacağımız modülleri dahil edebiliriz.

#ÖRN:

import math

math.factorial() #faktöriyel fonksiyonu

#dir(math) fonksiyonunu kullanarak math modülünün içerdiği fonksiyonların bir listesini görebiliriz.

#Ancak bu fonksiyonların nasıl kullanıldığını öğrenebilmek için ise help(math) şeklinde math modülünün bir nevi açıklaması olan kodlara erişebiliriz ve bu şekilde bu modül içerisinde bulunan fonksiyonların kullanımını öğrenebiliriz.

import math as matematik

#bu şekilde math modülünü programımıza dahil ediyoruz ancak kullanacağımız zaman matematik olarak kullanacağımızı da belirtiyoruz.

#Modülleri bir şekilde daha programımıza dahil edebiliriz:

from math import *

#buradaki yıldız işaretinin anlamı, modül içerisindeki her bir fonksiyonu dahil etmek istediğimizi belirtmiş oluyoruz.

#ve bu yöntemi kullandığımız zaman modülün içerisindeki fonksiyonları kullanmak için modülün adını da yazmamız gerekmez. 

#Yani math.factorial() yerine direkt olarak factorial() fonksiyonunu bu şekilde kullanabiliriz.

#Eğer modül içerisindeki bütün fonksiyonları değil de yalnızca kullanacağımız fonksiyonları dahil etmek istersek:

from math import floor,ceil

#ve bu şekilde yaptığımızda floor() ve ceil() fonksiyonları haricinde hiç bir fonksiyonu kullanamayız.

#KENDİ MODÜLLERİMİZİ NASIL YAZARIZ?

"""
Herhangi bir python dosyasının içerisine istediğimiz kadar fonksiyon, sınıf, obje vs yazıyoruz.

Daha sonra bu pyhton dosyasının içerisindeki fonksiyonları,sınıfları ve objeleri diğer programlarımızda kullanmak için bu dosyayı diğer programlarımıza import ediyoruz.

Yazdığımız modülümüze her yerden erişebilmek için, modül dosyamızı

C:\Python32\Lib

konumuna eklememiz gerekir.

"""


