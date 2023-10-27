import sys
from PyQt5 import QtWidgets

def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    


    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Dersleri")
    buton=QtWidgets.QPushButton(pencere)
    buton.setText("Basınız")
    etiket = QtWidgets.QLabel(pencere)
    etiket.setText("Merhaba Dünya")
    etiket.move(200,30)
    buton.move(199,80)




    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec_())

Pencere()