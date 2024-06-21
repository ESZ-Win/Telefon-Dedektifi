#Bu Program Emir Salih Zümrüt tarafından yazılmıştır
#This program writed by ESZ
from PyQt5.QtWidgets import *
from mainpage import MainPage

app = QApplication([])
pencere = MainPage()
pencere.show()
app.exec_()