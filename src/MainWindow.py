from PyQt4 import uic, QtCore
from PyQt4.QtCore import Qt, QMetaObject, Q_ARG, QString
from UserFactory import UserFactory
import InternetClient

qtcMainWindowFile = "mainwindow.ui"
Ui_MainWindow, MainWindowClass = uic.loadUiType(qtcMainWindowFile)

class MainWindow(MainWindowClass, Ui_MainWindow):
    def __init__(self, parent=None):
        MainWindowClass.__init__(self)
        Ui_MainWindow.__init__(self)
        self.parent = parent
        self.setupUi(self)

        self.uf = UserFactory('users.csv')

    def cardScanned(self, card):
        self.statusLabel.setText("Loading ...")

        userid = self.uf.read(card)[1]
        user = InternetClient.getUserDetails(userid)
        status = InternetClient.getUserStatus(userid, 0)
        statusDetails = None
        if status == "in":
            statusDetails = InternetClient.getUserStatus(userid, 1)
        QMetaObject.invokeMethod(self.parent, "startLogin", Qt.QueuedConnection, Q_ARG(int, userid), Q_ARG(QString, user["realname"]), Q_ARG(QString, status), Q_ARG(QString, user["last_visit"]))

        self.statusLabel.setText("")
