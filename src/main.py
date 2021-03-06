import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QString
from CardReaderThread import CardReaderThread
from MainWindow import MainWindow
from AddUserWindow import AddUserWindow
from LoginWindow import LoginWindow

class MyApp(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)
        self.setStyleSheet("background-color: #3190C3;")
        self.central_widget = QtGui.QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.mainWindow = MainWindow(self)
        self.mainWindow.addUserButton.clicked.connect(self.startAddUser)
        self.central_widget.addWidget(self.mainWindow)
        self.addUserWindow = None
        self.loginWindow = None
#        self.showFullScreen()

        self.threads = []
        self.cardReaderThread = CardReaderThread(self.mainWindow)
        self.threads.append(self.cardReaderThread)
        self.cardReaderThread.start()

#        self.startLogin()

    def startAddUser(self):
        self.addUserWindow = AddUserWindow(self)
        self.addUserWindow.backButton.clicked.connect(self.exitAddUser)
        self.cardReaderThread.changeParent(self.addUserWindow)
        self.central_widget.addWidget(self.addUserWindow)
        self.central_widget.setCurrentWidget(self.addUserWindow)

    def exitAddUser(self):
        self.central_widget.setCurrentWidget(self.mainWindow)
        self.central_widget.removeWidget(self.addUserWindow)      
        self.cardReaderThread.changeParent(self.mainWindow)
        self.addUserWindow = None

    @QtCore.pyqtSlot(QString, QString, QString, QString)
    def startLogin(self, id, realName, status, lastLogin):
        self.loginWindow = LoginWindow(self, id, realName, status, lastLogin)
        self.loginWindow.logoutButton.clicked.connect(self.exitLogin)
        self.cardReaderThread.changeParent(self.loginWindow)
        self.central_widget.addWidget(self.loginWindow)
        self.central_widget.setCurrentWidget(self.loginWindow)

    def exitLogin(self):
        self.central_widget.setCurrentWidget(self.mainWindow)
        self.central_widget.removeWidget(self.loginWindow)
        self.cardReaderThread.changeParent(self.mainWindow)
        self.loginWindow = None
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()

    sys.exit(app.exec_())
