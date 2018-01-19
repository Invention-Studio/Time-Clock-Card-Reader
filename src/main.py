import sys
from PyQt4 import QtGui

from CardReaderThread import CardReaderThread
from MainWindow import MainWindow
from AddUserWindow import AddUserWindow

class MyApp(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)
        self.setStyleSheet("background-color: #3190C3;")
        self.central_widget = QtGui.QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.mainWindow = MainWindow(self)
        self.mainWindow.addUserButton.clicked.connect(self.addUser)
        self.central_widget.addWidget(self.mainWindow)
        self.addUserWindow = None
        #self.showFullScreen()

        self.threads = []
        cardReaderThread = CardReaderThread(self)
        self.threads.append(cardReaderThread)
        cardReaderThread.start()

    def addUser(self):
        self.mainWindow.killCardReaderThread()
        if self.addUserWindow is None:
            self.addUserWindow = AddUserWindow(self)
        self.addUserWindow.backButton.clicked.connect(self.exitAddUser)
        self.central_widget.addWidget(self.addUserWindow)
        self.central_widget.setCurrentWidget(self.addUserWindow)
        self.addUserWindow.startCardReaderThread()

    def exitAddUser(self):
        self.addUserWindow.killCardReaderThread()
        self.central_widget.setCurrentWidget(self.mainWindow)
        self.central_widget.removeWidget(self.addUserWindow)      
        self.mainWindow.startCardReaderThread()
        
    def cardScanned(card):
        print card

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()

    sys.exit(app.exec_())
