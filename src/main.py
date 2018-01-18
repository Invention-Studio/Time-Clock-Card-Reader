import SerialRead as sr
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QHBoxLayout
from PyQt4.QtCore import Qt
 
qtCreatorFile = "mainwindow.ui"
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class CardReaderThread(QtCore.QThread):
    def __init__(self, lineedit):
        QtCore.QThread.__init__(self)
        self.lineedit = lineedit

    def run(self):
        card = None
        while True:
          card = sr.readCard()
          print card
          self.lineedit.setText(card)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #self.showFullScreen()

        self.threads = []
        reader = CardReaderThread(self.username_field)
        self.threads.append(reader)
        reader.start()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()

    sys.exit(app.exec_())
