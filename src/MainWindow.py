from PyQt4 import uic, QtCore, QtGui
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
        userid = self.uf.read(card)[1]
        user = InternetClient.getUserDetails(userid)
        status = InternetClient.getUserStatus(userid, 0)
        statusDetails = None
        if status == "in":
            statusDetails = InternetClient.getUserStatus(userid, 1)

        QMetaObject.invokeMethod(obj=self.parent, member="startLogin", type=Qt.QueuedConnection, value0=Q_ARG(QtGui.QMainWindow, self.parent), value1=Q_ARG(QString, user["realname"]), value2=Q_ARG(QString, status), value3=Q_ARG(int, user["last_visit"]))

#        self.parent.startLogin(user, status, statusDetails)
