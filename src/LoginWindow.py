from PyQt4 import uic, QtCore
from PyQt4.QtCore import QString

qtcLoginWindowFile = "loginwindow.ui"
Ui_LoginWindow, LoginWindowClass = uic.loadUiType(qtcLoginWindowFile)

class LoginWindow(LoginWindowClass, Ui_LoginWindow):
    def __init__(self, parent=None, id=None, realName=None, status=None, lastClockIn=None):
        LoginWindowClass.__init__(self)
        Ui_LoginWindow.__init__(self)
        self.parent = parent
        self.setupUi(self)

        self.id = id
        self.realName = realName
        self.status = status
        self.lastClockIn = lastClockIn

        self.nameLabel.setText("Hello, " + realName)
        if status == "in":
            self.clockButton.setText("Clock Out")
            self.clockButton.clicked.connect(self.clockout)
        else:
            self.clockButton.setText("Clock In")
            self.clockButton.clicked.connect(self.clockin)


    def logout(self):
        self.parent.exitLogin()

    def clockin(self):
        print "Clocking in " + self.id

    def clockout(self):
        print "Clocking out " + self.id

    @QtCore.pyqtSlot(QString)
    def cardScanned(self, card):
        pass
