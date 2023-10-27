import sys
from PyQt5 import QtWidgets,QtGui


def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Dersleri")
    etiket1 = QtWidgets.QLabel(pencere)
    #bir label oluşturup bunu da pencere üzerine ekliyoruz.
    etiket1.setText("Bu bir yazıdır.")
    #Bunu yaptığımızda yazımız pencerenin en sol üst köşesinde bulunur.
    etiket1.move(200,30)
    #move metodunu kullanarak label'ın pencere üzerindeki konumunu değiştirebiliriz.
    etiket2=QtWidgets.QLabel(pencere)
    #ikinci labelı oluşturuyoruz.
    etiket2.setPixmap(QtGui.QPixmap("C:/Users/Feyza/Desktop/Python_Dersleri/PyQt5/kopek1.jpg"))
    #ikinci etiketimiz bir resim. onu da bu şekilde penceremize ekledik.
    #resim yazının üstüne geldiği için konumunu değiştirelim:
    etiket2.move(150,70)
    pencere.setGeometry(100,100,500,500)
    #Burada pencereyi göstermeden önce, penceremizin açıldığında
    #masaüstünde hangi konumda olacağını ve boyutunu belirttik.
    #100,100 değerleri masaüstünde 100'e 100 konumundan başlamasını;
    #500,500 de penceremizin boyutunu belirler.
    pencere.show()
    sys.exit(app.exec_())

Pencere()