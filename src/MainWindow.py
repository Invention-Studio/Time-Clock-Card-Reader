from PyQt4 import uic, QtCore
from PyQt4.QtCore import QString
from UserFactory import UserFactory
import InternetClient

qtcMainWindowFile = "mainwindow.ui"
Ui_MainWindow, MainWindowClass = uic.loadUiType(qtcMainWindowFile)

class MainWindow(MainWindowClass, Ui_MainWindow):
    def __init__(self, parent=None):
        MainWindowClass.__init__(self)
        Ui_MainWindow.__init__(self)
        self.parent = parent
        self.something = "testing"
        self.setupUi(self)

        self.uf = UserFactory('users.csv')

    @QtCore.pyqtSlot(QString)
    def cardScanned(self, card):
        print self.something
        userid = self.uf.read(card)[1]
        user = InternetClient.getUserDetails(userid)
        status = InternetClient.getUserStatus(userid, 0)
        statusDetails = None
        if status == "in":
            statusDetails = InternetClient.getUserStatus(userid, 1)

        self.parent.startLogin(user["realname"], status, user["last_visit"])
