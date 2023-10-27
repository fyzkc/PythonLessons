import sys
from PyQt5 import QtWidgets
#QtWidgets pencere buton gibi özellikleri barındırır.

def Pencere():
    #pencere isminde bir fonksiyon yazalım.
    #pyqt programlarının içinde mutlaka bir adet uygulama nesnesinin olması gerekiyor.

    app = QtWidgets.QApplication(sys.argv)
    #QApplication sınıfından bir uygulama nesnesi ürettik.
    #nesnemize de parametre olarak komut satırından çalıştıracağımız zaman
    #kullanıcıdan aldığımız argümanları gönderdik.

    pencere=QtWidgets.QWidget()
    #QWidget sınıfından bir pencere oluşturduk.
    pencere.setWindowTitle("PyQt5 Dersleri")
    #penceremize bir isim verdik.
    pencere.show()
    #penceremizi app içerisinde gösterdik.
    sys.exit(app.exec_())
    #çarpı tuşuna basmadığımız sürece uygulamamızın çalışmasını sağlar.

Pencere()