from PyQt4 import uic
from UserFactory import UserFactory

qtcMainWindowFile = "adduserwindow.ui"
Ui_AddUserWindow, AddUserWindowClass = uic.loadUiType(qtcMainWindowFile)

class AddUserWindow(AddUserWindowClass, Ui_AddUserWindow):
    def __init__(self, parent=None):
        AddUserWindowClass.__init__(self)
        Ui_AddUserWindow.__init__(self)
        self.setupUi(self)

        uf = UserFactory('users.csv')
        users = uf.readAll()
        print len(users)

        self.userDropdown.addItem('Kabbabe, Kristian (kakaday22)', 123)
        self.userDropdown.addItem('Rupert, Nick (nickrupert7)', 789)

    def cardScanned(self, card):
        print "AddUserWindow: " + card
