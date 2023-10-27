"""
Requests ve BeautifulSoup modülleri internetten veri çekmeyi ve bu verileri
parçalamayı sağlar.
Ancak bunlar pythonda hazır olmadığından internetten indirmemiz gerekiyor.

"""
#Windows cmd üzerinden indirmek için şu komutları kullanacağız:

# pip3 install requests
# pip3 install beautifulsoup4

#Bu modüller ile web sayfalarındaki verileri alabiliriz.

#Web sayfalarından veri çekmek için HTML bilmek gerekli.
#HTML için göz atabilecek sayfalar:

# http://www.htmldersleri.org/index.php?getir=html_intro&ID=1

# http://www.htmldersleri.org/index.php?getir=html_links&ID=7

# http://www.htmldersleri.org/index.php?getir=html_attributes&ID=4

# http://www.htmldersleri.org/index.php?getir=html_tables&ID=9


#Veri alacağımız web sitesi: 
#https://tr.wikipedia.org/

import requests
from bs4 import BeautifulSoup

#web sayfasındaki verileri requests ile çekip, bilgileri de beautifulsoup ile almaya çalışacağız.

response = requests.get("https://tr.wikipedia.org/")
#print(response)
#sayfaya istek yaptığımızda başarılı bir cevap almak için 200 request kodunun dönmesi lazım.

htmlIcerigi=response.content
#content özelliği HTML dökümanının içeriğini almayı sağlar.
#Bu içeriğin HTML sayfa içeriğini bu şekilde alırız.
#Ancak bunu daha güzel gösterebilmek için beautifulsoup modülünü kullanacağız.

soup= BeautifulSoup(htmlIcerigi,"html.parser")
#soup objesinin ilk parametresi html içeriği ve html içeriğini parçalayacağımız için de html.parser olacak.

#print(soup.prettify())
#web sayfasının kodlarını daha güzel görüntelemek için prettify() fonksiyonunu kullanacağız.

#Bu şekilde html kodları çok daha düzenli gözüküyor.

#Web sayfası üzerindeki etiketleri çekmek için artık requests modülünü değil,
#beautifulsoup modülünü kullanacağız.

#Web sayfası üzerindeki tüm linkleri getirmek isteyelim.
#Bunun için sayfa üzerindeki tüm a etiketlerini çekmemiz lazım.


#print(soup.find_all("a"))

#find_all() fonksiyonu içerisine aldığı değere göre verileri bir liste şeklinde döndürür.

#Daha güzel göstermek için:

# for i in soup.find_all("a"):
#     print(i)
#     print("-----------------")

#Bu şekilde tüm a etiketleri liste olarak gelir.

#a etiketlerinin sadece href özelliği olanları almak istersek:

#NOT: linkler a href etiketi ile verilir.
#geri kalan a etiketleri class vs kodları da içerebilir.
#biz sadece link istediğimiz için a href olanları çekmek istiyoruz.

# for i in soup.find_all("a"):
#     print(i.get("href"))
#     print("-----------------")

#Bu şekilde HTML etiketleri olmadan a href etiketlerinin değerlerini almış oluyoruz.

#a etiketleri içerisinden yalnızca yazıları çekmek istersek:


# for i in soup.find_all("a"):
#     print(i.text)
#     print("-----------------")

#Bu yazılar, üzerine basıldığında bir linke yönlendiren yazılardır.

#Site içerisinde herhangi bir yeri almak istersek, o yerin site içerisindeki
#konumunu bilmemiz gerekir.
#Örneğin vikipedi sayfasındaki tarihte bugün kısmı bir td etiketi içerisinde duruyor.
#ve id bilgisi mp-itn şeklinde.
#o halde id bilgisi mp-itn olan verileri çekmek istersek biz bu kısma ulaşmış oluruz.


print(soup.find_all("td",{"id":"mp-itn"}))

#burada görüldüğü gibi bir sözlük tipi verdik parametre olarak.
#id değeri mp-itn olan td etiketlerini getir demek istiyoruz bu şekilde

