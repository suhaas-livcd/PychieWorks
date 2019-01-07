# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QMessageBox,QMainWindow, QPushButton, QAction, QLineEdit, QMessageBox, QPlainTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
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
        self.textbox_Diary = QPlainTextEdit(self)
        self.textbox_Diary.move(20, 80)
        self.textbox_Diary.resize(280,100)
        self.textbox_Diary.insertPlainText("Dear diary,\nn\nBeauty...\n\nI learn...\n\nThoughts...")        
        # Create a button in the window
        self.button = QPushButton('Commit your day', self)
        self.button.move(20,400)
         
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
#        self.setFocus()
        self.show()

    @pyqtSlot()
    def on_click(self):
        textbox_WordOfDayValue = self.textbox_WordOfDay.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textbox_WordOfDayValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox_WordOfDay.setText("")
        
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
