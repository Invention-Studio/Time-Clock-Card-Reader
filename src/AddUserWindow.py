from SerialReader import SerialReader
from PyQt4 import QtCore, uic

qtcMainWindowFile = "adduserwindow.ui"
Ui_AddUserWindow, AddUserWindowClass = uic.loadUiType(qtcMainWindowFile)

class CardReaderThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)


    def run(self):
        reader = SerialReader("COM6")
        card = ""
        while True:
          if reader.isFound():
              card = reader.readCard()

class AddUserWindow(AddUserWindowClass, Ui_AddUserWindow):
    def __init__(self, parent=None):
        AddUserWindowClass.__init__(self)
        Ui_AddUserWindow.__init__(self)
        self.setupUi(self)
        self.userDropdown.addItem('Kabbabe, Kristian (kakaday22)', 123)
        self.userDropdown.addItem('Rupert, Nick (nickrupert7)', 789)

        self.threads = []
        reader = CardReaderThread()
        self.threads.append(reader)
        reader.start()
