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

        for u in users:
            id = u[0]
            lastname = u[2]
            if lastname != "":
                lastname = lastname + ", "
            firstname = u[1]
            username = u[3]
            entry = lastname + firstname + " (" + username + ")"
            self.userDropdown.addItem(entry, id)

        

    def cardScanned(self, card):
        index = self.userDropdown.currentIndex()
        print self.userDropdown.itemData(index).toInt()[0]
