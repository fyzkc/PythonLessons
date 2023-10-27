"""
Mail atmak için bir tane SMTP serverına ihtiyacımız var.
Biz Gmail Server'ına bağlanarak mail atma işlemlerini gerçekleştireceğiz.

"""

# upuzhlzuuwqeeqgh uygulama şifresi

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

#İlk olarak mail yapımızı oluşturarak başlıyoruz:

mesaj=MIMEMultipart()

mesaj["From"] = "koc.feyza.fb@gmail.com"
#From parametresi bu kütüphane içerisinde mail kaynağı için kullanılır.

mesaj["To"] = "koc.feyza.fb@gmail.com"
#To ğarametresi de bu kütüphane içerisinde mailin gideceği adresi almak için kullanılır.

mesaj["Subject"] = "SMTP Dersi" 
#mailin konusunu yazdık

#Şimdi de mail içeriğini oluşturmamız gerekiyor.

mail="""

SMTP ile mail gönderiyorum.
Feyza Koç

"""

mesajGovdesi = MIMEText(mail,"plain")
#mailin içeriği için MIMEText modülünden yararlanıyoruz.
#göndereceğimiz maili ve hangi formatta göndereceğimizi yazıyoruz.
#plain text, normal yazı olarak göndermeyi sağlıyor.

mesaj.attach(mesajGovdesi)
#mesaj gövdemizi mesaj yapımıza ekledik.

#mesajı oluşturduğumuz için şimdi bir server'a bağlanıp bunu atmaya çalışalım.

#olası hatalar için try bloğunda yazalım:

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)
    #server ismini ve port numarasını verdik.

    mail.ehlo()
    #servera kendimizi tanıtıyoruz.

    mail.starttls()
    #verilerin şifrelenmesi için

    mail.login("koc.feyza.fb@gmail.com","Kaputdrakonis01_")
    #login işlemiyle server'a bağlandık.

    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
    #mesajı, kimden geldiği, kime gittiği ve mesaj içeriği bilgileriyle gönderiyoruz.
    #mesaj multiple text formatında olduğundan stringe çevirip yapıyoruz.

    print("mail başarıyla gönderildi.")

    mail.close()
    #smtp serverından bağlantıyı kesiyoruz.

except:
    sys.stderr.write("Bir sorun oluştu")
    sys.stderr.flush()


#NOT: Gmail adresim iki adımlı doğrulama içerdiği için bu işlemi gerçekleştiremiyorum.
