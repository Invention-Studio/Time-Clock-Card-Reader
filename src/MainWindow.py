from SerialReader import SerialReader
from PyQt4 import QtCore, uic

qtcMainWindowFile = "mainwindow.ui"
Ui_MainWindow, MainWindowClass = uic.loadUiType(qtcMainWindowFile)

class CardReaderThread(QtCore.QThread):
    def __init__(self, lineedit):
        QtCore.QThread.__init__(self)
        self.lineedit = lineedit

    def run(self):
        self.reader = SerialReader("COM6")
        card = ""
        while True:
          if self.reader.isFound():
              card = self.reader.readCard()
              self.lineedit.setText(card)

    def close(self):
        print "Closing MainWindow CardReaderThread"
        self.reader.close()
        self.terminate()

class MainWindow(MainWindowClass, Ui_MainWindow):
    def __init__(self, parent=None):
        MainWindowClass.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.threads = []
        self.startCardReaderThread()

    def killCardReaderThread(self):
        self.cardReaderThread.close()
        self.threads.remove(self.cardReaderThread)
        del self.cardReaderThread
        self.cardReaderThread = None

    def startCardReaderThread(self):
        self.cardReaderThread = CardReaderThread(self.username_field)
        self.threads.append(self.cardReaderThread)
        self.cardReaderThread.start()

