# Proje 1
# Bilgisayarınızdaki tüm mp4,txt ve pdf dosyalarını os modülüyle arayın ve bunların nerede bulunduklarını 
# ve isimlerini ayrı ayrı "pdf_dosyalari.txt","mp4_dosyaları.txt","txt_dosyaları.txt" adlı dosyalara kaydedin.

import os

txt = open("C:/Users/Feyza/Desktop/Python_Dersleri/Ileri_Seviye_Moduller/txt_dosyalari.txt","w",encoding="utf-8")
mp4 = open("C:/Users/Feyza/Desktop/Python_Dersleri/Ileri_Seviye_Moduller/mp4_dosyalari.txt","w",encoding="utf-8")
pdf = open("C:/Users/Feyza/Desktop/Python_Dersleri/Ileri_Seviye_Moduller/pdf_dosyalari.txt","w",encoding="utf-8")


for klasorYolu,klasorIsimleri,dosyaIsimleri in os.walk("C:/Users/Feyza"):
    for i in dosyaIsimleri:
        if(i.endswith(".txt")):
            txt.write(i)
            txt.write("\n")
        elif(i.endswith(".mp4")):
            mp4.write(i)
            mp4.write("\n")
        elif(i.endswith(".pdf")):
            pdf.write(i)
            pdf.write("\n")

txt.close()
mp4.close()
pdf.close()