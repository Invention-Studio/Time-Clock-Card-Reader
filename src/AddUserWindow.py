from SerialReader import SerialReader
from PyQt4 import QtCore, uic

qtcMainWindowFile = "adduserwindow.ui"
Ui_AddUserWindow, AddUserWindowClass = uic.loadUiType(qtcMainWindowFile)

class CardReaderThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)

    def run(self):
        self.reader = SerialReader("COM6")
        card = ""
        while True:
          if self.reader.isFound():
              card = self.reader.readCard()

    def close(self):
        self.reader.close()

class AddUserWindow(AddUserWindowClass, Ui_AddUserWindow):
    def __init__(self, parent=None):
        AddUserWindowClass.__init__(self)
        Ui_AddUserWindow.__init__(self)
        self.setupUi(self)
        self.userDropdown.addItem('Kabbabe, Kristian (kakaday22)', 123)
        self.userDropdown.addItem('Rupert, Nick (nickrupert7)', 789)
        self.threads = []
        self.startCardReaderThread()

    def killCardReaderThread(self):
        self.cardReaderThread.close()
        self.cardReaderThread.terminate()
        self.threads.remove(self.cardReaderThread)
        del self.cardReaderThread
        self.cardReaderThread = None

    def startCardReaderThread(self):
        self.cardReaderThread = CardReaderThread()
        self.threads.append(self.cardReaderThread)
        self.cardReaderThread.start()



