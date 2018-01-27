from PyQt4 import uic
from UserFactory import UserFactory
import InternetClient

qtcMainWindowFile = "mainwindow.ui"
Ui_MainWindow, MainWindowClass = uic.loadUiType(qtcMainWindowFile)

class MainWindow(MainWindowClass, Ui_MainWindow):
    def __init__(self, parent=None):
        MainWindowClass.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.uf = UserFactory('users.csv')

    def cardScanned(self, card):
        print self.uf.read(card[1])
        InternetClient.getUserStatus(self.uf.read(card[1]))
