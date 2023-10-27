#Pillow modülü cmd üzerinden indirmek için:

#pip3 install Pillow


from PIL import Image,ImageFilter

resim= Image.open("C:/Users/Feyza/Desktop/Python_Dersleri/Ileri_Seviye_Moduller/kopek1.jpg")
#resim.show() #Resmi açtık.

#image.save("kopek_.jpg")
#kopek resmini kopek_ olarak farklı kaydedelim.

dondurDoksan=resim.rotate(90)
#resmi 90 derece döndürür.
#dondurDoksan.show()

#resimlerin sadece siyah beyaz halini almak için:
siyah_beyaz=resim.convert(mode="L")
#siyah_beyaz.show()

#resimlerin boyutlarını istediğimiz ölçülerde değiştirebiliriz:
boyut=(960,600)
#resim.thumbnail(boyut)
#resim.save("kopek_thumbnail.jpg")
#bu şekilde thumbnail haline getirdik.
#ve başka bir jpg dosyası olarak yeniden kaydettik.

#resim.show()

#Resimleri belirli bir ölçüde blurlamak için:
blur= resim.filter(ImageFilter.GaussianBlur(5))
#İçine yazdığımız değere göre resmin blurlaması az veya çok olur.
#blur.show()

#Resimleri kırpma:

#Resimleri kırpmak için öncelikle resimlerin kırpılacağı yerlerin koordinasyonlarını bilmemiz gerekiyor.
#Ancak ben şu an koordinatlarını bulabileceğim bir uygulama kullanmadığım için kafama göre yapacağım.

ikinci_resim= Image.open("C:/Users/Feyza/Desktop/Python_Dersleri/Ileri_Seviye_Moduller/kopek2.jpg")

alan= (700,0,1500,1000)

kirpilan = ikinci_resim.crop(alan)
kirpilan.show()