from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QCalendarWidget
from PyQt5 import uic
import sys
#from persiantools.jdatetime import JalaliDate
import jdatetime
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        #load the ui file
        uic.loadUi("calendarme.ui",self)
        self.setWindowTitle("calender")
        #define our widgets
        self.label=self.findChild(QLabel,"label")
        self.miladi=self.findChild(QCalendarWidget,"calendarWidget")
        self.shamsi=self.findChild(QCalendarWidget,"shamsi")
        #convert date to shamsi at the run time
        self.miladi_to_shamsi()
        #convert date to shamsi by click on every date in miladi calendar
        self.miladi.selectionChanged.connect(self.miladi_to_shamsi)    
        #show the App
        self.show()    
    #Define function to convert miladi to shamsi
    def miladi_to_shamsi(self):
         #put date in variable
         dateselected=self.miladi.selectedDate().toPyDate() 
         #seprate year ,month and day of date
         year=dateselected.year
         month=dateselected.month
         day=dateselected.day   
         #define start date   
         l_date = QDate(1300, 1, 1)
         self.shamsi.setMinimumDate(l_date)
         #convert date to shamsi
         jalali_date = jdatetime.date.fromgregorian(day=day ,month=month,year=year)
         self.label.setText(jdatetime.date.fromgregorian(day=day ,month=month,year=year).strftime("%A  %B "))
         self.shamsi.setCurrentPage(jalali_date.year,jalali_date.month)
          

#initialize the app
app=QApplication(sys.argv)
UIWindow=UI()
app.exec_()