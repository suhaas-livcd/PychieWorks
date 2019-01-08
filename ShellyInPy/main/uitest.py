# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QMessageBox, QCheckBox
from PyQt5.QtWidgets import QPlainTextEdit, QLabel, QMainWindow, QPushButton, QAction, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt, QSize
from ShellyInPy.main.utils import definedUtils
class Example(QMainWindow):
    
    def __init__(self):
        super().__init__() 
        self.title = 'My Shelly in Pie'               
        self.initUI()
        print("____init____ function")
        
    def initUI(self):  
        print("__initUI__ function")   
        self.setWindowTitle(self.title)                  
        self.resize(500, 500)
        self.center() 
        self.statusBar().showMessage('Message in statusbar.')
        # Create textbox_WordOfDay
        self.textbox_WordOfDay = QLineEdit(self)
        self.textbox_WordOfDay.move(20, 20)
        self.textbox_WordOfDay.resize(280,40)
        self.textbox_WordOfDay.setPlaceholderText("A word that describes the best of your day")
        #Create textbox_Dairy
        #Tooltip since no multiline place holder in 
        # ,\nBeauty...\nI learn...\nThoughts...
        self.textbox_Diary = QPlainTextEdit(self)
        self.textbox_Diary.move(20, 80)
        self.textbox_Diary.resize(280,320)
        self.textbox_Diary.setPlaceholderText("Dear diary,...")        

        #Differnt labels
        self.label_TodayDate = QLabel(self)
        todayDateIs = definedUtils.todayDate(self)
        self.label_TodayDate.setText(todayDateIs)
        self.label_TodayDate.move(320,20)

        start_y=50
        self.label_seperator_1 = QLabel(self)
        self.label_seperator_1.setText("____Priorities____")
        self.label_seperator_1.move(320,start_y)        
        
        #Different checkbox
        start_y=start_y+20
        self.cb_Ielts = QCheckBox("I.E.L.T.S",self)
        self.cb_Ielts.move(320,start_y)
#        self.b.stateChanged.connect(self.clickBox)
        
        self.cb_Guitar = QCheckBox("Guitar",self)
        start_y=start_y+20
        self.cb_Guitar.move(320,start_y)
        
        self.cb_Charcaol = QCheckBox("Charcoal",self)
        start_y=start_y+20
        self.cb_Charcaol.move(320,start_y)
        
        self.label_seperator_2 = QLabel(self)
        self.label_seperator_2.setText("____Projects____")
        start_y=start_y+40
        self.label_seperator_2.move(320,start_y)    
        
        self.cb_Letterie = QCheckBox("Letterie",self)
        start_y=start_y+20
        self.cb_Letterie.move(320,start_y)
        
        self.cb_Bariechol = QCheckBox("Bariechol",self)
        start_y=start_y+20
        self.cb_Bariechol.move(320,start_y)
        
        self.cb_Shellie = QCheckBox("Shellie",self)
        start_y=start_y+20
        self.cb_Shellie.move(320,start_y)
        
        self.cb_Blog = QCheckBox("suhaas-livcd",self)
        start_y=start_y+20
        self.cb_Blog.move(320,start_y)
        
        self.label_seperator_3 = QLabel(self)
        self.label_seperator_3.setText("____Skills____")
        start_y=start_y+40
        self.label_seperator_3.move(320,start_y)    
        
        self.cb_CV = QCheckBox("CV - Py",self)
        start_y=start_y+20
        self.cb_CV.move(320,start_y)
        
        self.cb_DS = QCheckBox("Data Science",self)
        start_y=start_y+20
        self.cb_DS.move(320,start_y)
        
        self.cb_Edit = QCheckBox("Video and Photo Editting",self)
        start_y=start_y+20
        self.cb_Edit.move(320,start_y)
        
        self.label_seperator_4 = QLabel(self)
        self.label_seperator_4.setText("____Others____")
        start_y=start_y+40
        self.label_seperator_4.move(320,start_y)    
        
        self.cb_Camera = QCheckBox("Camera - 50K",self)
        start_y=start_y+20
        self.cb_Camera.move(320,start_y)
        
        self.cb_Everest = QCheckBox("Everest - 60 K",self)
        start_y=start_y+20
        self.cb_Everest.move(320,start_y)
        
        self.cb_Run = QCheckBox("Running",self)
        start_y=start_y+20
        self.cb_Run.move(320,start_y)
        
#        self.b.stateChanged.connect(self.clickBox)
        
        # Create a button in the window
        self.button = QPushButton('Commit', self)
        self.button.move(20,420)
        self.button.clicked.connect(self.on_click)
        self.button.setToolTip("<b>Commits</b> to git repo")
        self.setFocus()
        self.show()

#    def clickBox(self, state):
#        if state == Qt.Checked:
#            print('Checked')
#        else:
#            print('Unchecked')
            
    @pyqtSlot()
    def on_click(self):
        textbox_WordOfDayValue = self.textbox_WordOfDay.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textbox_WordOfDayValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox_WordOfDay.setText("")
        if self.cb_Everest.isChecked():
            print("Great to go")
        else:
            print("Oops")
        
        
    def center(self):     
        print("__center__ function")
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        print("__closeEvent__ function")
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()         
        
if __name__ == '__main__':
    print("__main__ function")
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
