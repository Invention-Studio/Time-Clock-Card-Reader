from PyQt4 import uic

qtcMainWindowFile = "adduserwindow.ui"
Ui_AddUserWindow, AddUserWindowClass = uic.loadUiType(qtcMainWindowFile)

class AddUserWindow(AddUserWindowClass, Ui_AddUserWindow):
    def __init__(self, parent=None):
        AddUserWindowClass.__init__(self)
        Ui_AddUserWindow.__init__(self)
        self.setupUi(self)
        self.userDropdown.addItem('Kabbabe, Kristian (kakaday22)', 123)
        self.userDropdown.addItem('Rupert, Nick (nickrupert7)', 789)

    def cardScanned(card):
        print "AddUserWindow: " + card
