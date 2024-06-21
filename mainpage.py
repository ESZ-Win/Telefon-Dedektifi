#Ana Yönetim Kodları

import opencage
import os
import folium#Haritada işaretlemek için kullanılan modül
from PyQt5.QtWidgets import *
from phone import Ui_MainWindow
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import webbrowser as wb

class MainPage(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        self.mainpage= Ui_MainWindow()
        self.mainpage.setupUi(self)
        self.mainpage.konumBtn.clicked.connect(self.OnClickedKonumBtn)
        self.mainpage.getValue.clicked.connect(self.OnClickedGvBtn)    
        self.mainpage.konumText.setText("")
        self.mainpage.gsmText.setText("")
        self.key =""#Buraya opencage sitesine kayıt olduğunuzda api key i yazın
        self.geocoder=OpenCageGeocode(self.key)
        self.mainpage.resInfo.clicked.connect(self.OnClickedResBtn)
    def OnClickedGvBtn(self):
        self.number = self.mainpage.lineEdit.text()#Girilen Numara
        self.newnumber = phonenumbers.parse(self.number)
        self.gsm=carrier.name_for_number(self.newnumber, "tr")
        self.location = geocoder.description_for_number(self.newnumber,"tr")
        self.mainpage.konumText.setText("Konum: "+self.location)
        self.mainpage.gsmText.setText("GSM:"+self.gsm)
    def OnClickedKonumBtn(self):
        self.number = self.mainpage.lineEdit.text()#Girilen Numara
        self.newnumber = phonenumbers.parse(self.number)
        self.location = geocoder.description_for_number(self.newnumber,"tr")
        self.query=str(self.location)
        self.res=self.geocoder.geocode(self.query)
        self.lat = self.res[0]['geometry']['lat']
        self.lng = self.res[0]['geometry']['lng']
        print(self.lat,self.lng)
        self.phoneMap = folium.Map(location=[self.lat,self.lng],zoom_start=9)
        folium.Marker([self.lat,self.lng],popup=self.location).add_to(self.phoneMap)
        self.phoneMap.save("phoneloc.html")
        wb.open("phoneloc.html")
    def OnClickedResBtn(self):
        os.remove("phoneloc.html")
        self.mainpage.konumText.setText("")
        self.mainpage.gsmText.setText("")
        self.mainpage.lineEdit.setText("")
        
        
        
    
