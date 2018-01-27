from PyQt4 import uic
from UserFactory import UserFactory

qtcMainWindowFile = "mainwindow.ui"
Ui_MainWindow, MainWindowClass = uic.loadUiType(qtcMainWindowFile)

class MainWindow(MainWindowClass, Ui_MainWindow):
    def __init__(self, parent=None):
        MainWindowClass.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

    def cardScanned(self, card):
        var uf = UserFactory()
        print uf.read(card)
