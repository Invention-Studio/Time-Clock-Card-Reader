from PyQt4 import uic, QtCore
from PyQt4.QtCore import QString

qtcLoginWindowFile = "loginwindow.ui"
Ui_LoginWindow, LoginWindowClass = uic.loadUiType(qtcLoginWindowFile)

class LoginWindow(LoginWindowClass, Ui_LoginWindow):
    def __init__(self, parent=None, realName=None, status=None, lastClockIn=None):
        LoginWindowClass.__init__(self)
        Ui_LoginWindow.__init__(self)
        self.parent = parent
        self.setupUi(self)

        self.nameLabel.text = "Hello, " + realName
        if status == "in":
            self.clockButton.text = "Clock Out"
        else:
            self.clockButton.text = "Clock In"

        print realName
        print status
        print lastClockIn

    def logout(self):
        self.parent.exitLogin()

    @QtCore.pyqtSlot(QString)
    def cardScanned(self, card):
        pass
