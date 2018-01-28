from PyQt4 import uic, QtCore
from PyQt4.QtCore import QString
from UserFactory import UserFactory
from threading import Timer

qtcMainWindowFile = "adduserwindow.ui"
Ui_AddUserWindow, AddUserWindowClass = uic.loadUiType(qtcMainWindowFile)

class AddUserWindow(AddUserWindowClass, Ui_AddUserWindow):
    def __init__(self, parent=None):
        AddUserWindowClass.__init__(self)
        Ui_AddUserWindow.__init__(self)
        self.setupUi(self)

        self.uf = UserFactory('users.csv')
        users = self.uf.readAll()

        for u in users:
            id = u[0]
            lastname = u[2]
            if lastname != "":
                lastname = lastname + ", "
            firstname = u[1]
            username = u[3]
            entry = lastname + firstname + " (" + username + ")"
            self.userDropdown.addItem(entry, id)
		
    @QtCore.pyqtSlot(QString)
    def cardScanned(self, card):
        index = self.userDropdown.currentIndex()
        userid = self.userDropdown.itemData(index).toInt()[0]
        self.uf.overwrite(userid, card)
        self.statuslabel.setText("Successfully added " + self.userDropdown.currentText())
        t = Timer(3.0, self.successDissapear)
        t.start()
	
    def successDissapear(self):
        self.statuslabel.setText("")
