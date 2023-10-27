import requests
from bs4 import BeautifulSoup

# NOT: bu siteden veri çekemiyoruz, erişim hatası alıyoruz. 
#Ancak yine de konuyu öğrenmek adına kodlarını yazalım.


url = "https://www.imdb.com"

response = requests.get(url)

print(response)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi, "html.parser")

#Filmlerin td etiketleri altında olduklarını görüyoruz.
#Filmlerin özellikleri şöyle sıralanmış:

#1- filmin posteri: td etiketi altında class="posterColumn" değerine sahip
#2- filmin ismi: td etiketi altında class="titleColumn" değerine sahip
#3- filmin imdb puanı: td etiketi altında class="ratingColumn imdbRating" değerine sahip
#4- filme vereceğimiz puan: td etiketi altında class="ratingColumn" değerine sahip
#5- watchlist butonu: td etiketi altında class="watchlistColumn" değerine sahip

#Öncelikle filmlerin isimlerini alalım.

# for i in soup.find_all("td",{"class":"titleColumn"}):
#     print(i.text)
#     print("----------------------------")


basliklar= soup.find_all("td",{"class":"titleColumn"})

#şimdi de imdb puanlarının olduğu kısmı alalım.

ratingler= soup.find_all("td",{"class":"ratingColumn imdbRating"})

#Şimdi bu iki listeyi birleştirelim.
#Bunun için zip() fonksiyonunu kullanabiliriz.

for baslik,rating in zip(basliklar,ratingler):
    baslik=baslik.text
    rating=rating.text

    baslik=baslik.strip() #isimlerin başlarındaki ve sonlarındaki boşlukları silelim.
    baslik=baslik.replace("\n","") #alt satıra inme karakterlerinin yerine boşluk karakterini koyduk.

    rating=rating.strip()
    rating=rating.replace("\n","") 

    print("Film:",baslik.text)
    print("Puan:",rating.text)

#Kullanıcıdan bir değer alıp, alınan değerden daha yüksek puana sahip olan filmleri listeleyelim.

a= float(input("Puan girin: "))

if(float(rating)>a):
    print("Film:",baslik,"Puan:",rating)
    
