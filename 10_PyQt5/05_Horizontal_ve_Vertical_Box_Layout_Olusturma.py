import sys
from PyQt5 import QtWidgets

#Horizontal Box Layout: Elementleri yatay bir şekilde yerleştirebildiğimiz
#layout türüdür.
#Vertical Box Layout: Elementleri dikey bir şekilde yerleştirebildiğimiz
#layput türüdür.

def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    okay_butonu= QtWidgets.QPushButton("Tamam")
    #burada butonumuzu direkt olarak oencereye eklemeyeceğiz.
    #butonu layoutlara yerleştirip layoutları daha sonra pencereye yerleştireceğiz.
    #bu yüzden oluştururken parantez içerisinde pencere yazmadık.
    #onun yerine butonun textini verebiliriz.
    cancel_butonu=QtWidgets.QPushButton("İptal")

    h_box = QtWidgets.QHBoxLayout()
    #bir adet horizontal box layout oluşturduk.
    h_box.addWidget(okay_butonu)
    h_box.addWidget(cancel_butonu)
    #butonlarımızı horizontal box layout'umuza ekledik.
    h_box.addStretch()
    #elementlerin sola yaslanmış şekilde durmasını sağlar.

    #NOT: addStrecth() metodu aslında boşluk oluşturmayı sağlar.
    #Biz eğer ki bu metodu elementlerimizi oluşturduktan sonra çağırırsak,
    #elementlerimiz önce oluşturulur sonrasında boşluk oluşturulur.
    #böylece de elementler sola yaslanmış olur.
    #ancak elementleri oluşturmadan önce çağırırsak da önce boşluk oluşur sonrasında
    #elementler oluşur.
    #böylelikle de elementler sağa yaslanmış olur.
    
    #Ne tarafa yaslanırsa yaslansın pencerenin boyutunu değiştirdiğimizde hep aynı yerde kalır.

    #Eğer hem elementlerden önce hem de sonra kullanırsak da elementlerimizi
    #pencere içerisinde ortalamış oluruz. ve pencerenin boyutunu değiştirsek bile hep ortada kalırlar.
    #ancak bu olayların hepsi yatay olarak olacaktır.
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Dersleri")
    
    pencere.setLayout(h_box)
    #horizontal box layout'u da pencereye ekledik.

    pencere.setGeometry(100,100,500,500)
    pencere.show()


    sys.exit(app.exec_())

Pencere()