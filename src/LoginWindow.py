from PyQt4 import uic

qtcLoginWindowFile = "loginwindow.ui"
Ui_LoginWindow, LoginWindowClass = uic.loadUiType(qtcLoginWindowFile)

class LoginWindow(LoginWindowClass, Ui_LoginWindow):
    def __init__(self, parent=None):
        LoginWindowClass.__init__(self)
        Ui_LoginWindow.__init__(self)
        self.parent = parent
        self.setupUi(self)

    def logout(self):
        self.parent.exitLogin()

    def cardScanned(self, card):
        pass