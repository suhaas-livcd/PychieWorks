# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QMessageBox, QCheckBox, QShortcut
from PyQt5.QtWidgets import QPlainTextEdit, QLabel, QMainWindow, QPushButton, QAction, QLineEdit
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import pyqtSlot, Qt, QSize
from utils import definedUtils
from fileMgr import FileManager
from gitMgr import GitManager
from gitProcess import gitProcess

class Example(QWidget):
    
    def __init__(self):
        super().__init__() 
        self.initUI()
        self.shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.shortcut.activated.connect(self.on_open)
    
    @pyqtSlot()
    def on_open(self):
        print("Closing!")
        self.close()
    
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
            
    def initUI(self):  
        print("__initUI__ function")
        self.title = 'ShellyInPie 1.0'               
        self.setWindowTitle(self.title)                  
        self.resize(500, 500)
        self.center() 
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
        textbox_WordOfDay = self.textbox_WordOfDay.text()

        #Get data
        self.getData()
        print(self.my_data)
        
        #Creating a json file with data inside
        fileStatus=FileManager().createFile(self.my_data,json=True)
        
        #Committing data to git
        self.git_processThread = gitProcess(dirPath="/home/suhaas/Desktop/MyPrepLogger", commitMsg=textbox_WordOfDay)
        self.git_processThread.signal.connect(self.finished)
        self.git_processThread.start()

        QMessageBox.question(self, 'Message - from Shelly', 
            "\nFile Status: \n" + fileStatus,
            QMessageBox.Ok, QMessageBox.Ok)

    def finished(self, result):
        QMessageBox.question(self, 'Message - from Shelly', 
            "\nGit  Status: \n"+"Finished : "+result,
            QMessageBox.Ok, QMessageBox.Ok)

    def getData(self):
        self.my_data={}
        
        #Data from the text boxes
        self.my_data['textbox_WordOfDay'] = self.textbox_WordOfDay.text()
        self.my_data['textbox_Diary'] = self.textbox_Diary.toPlainText()
        
        #Data from checkbox
        self.my_data['cb_Ielts']=self.cb_Ielts.isChecked()
        self.my_data['cb_Guitar']=self.cb_Guitar.isChecked()
        self.my_data['cb_Charcaol']=self.cb_Charcaol.isChecked()
        self.my_data['cb_Letterie']=self.cb_Letterie.isChecked()
        self.my_data['cb_Bariechol']=self.cb_Bariechol.isChecked()
        self.my_data['cb_Shellie']=self.cb_Shellie.isChecked()
        self.my_data['cb_Blog']=self.cb_Blog.isChecked()
        self.my_data['cb_CV']=self.cb_CV.isChecked()
        self.my_data['cb_DS']=self.cb_DS.isChecked()
        self.my_data['cb_Edit']=self.cb_Edit.isChecked()
        self.my_data['cb_Camera']=self.cb_Camera.isChecked()
        self.my_data['cb_Everest']=self.cb_Everest.isChecked()
        self.my_data['cb_Run']=self.cb_Run.isChecked()
        
        print("Data retrieved from "+str(len(self.my_data))+ " elements")
        
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
    print(sys.path)
    try:
        App
    except:
        App = QApplication(sys.argv)
    ex = Example()
    sys.exit(App.exec_())
