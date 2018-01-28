from SerialReader import SerialReader
from PyQt4 import QtCore
from PyQt4.QtCore import Qt, QMetaObject, Q_ARG, QString

class CardReaderThread(QtCore.QThread):
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self)
        self.parent = parent

    def run(self):
        self.reader = SerialReader("COM6")
        card = ""
        while True:
          if self.reader.isFound():
              card = self.reader.readCard()
              QMetaObject.invokeMethod(self.parent, "cardScanned", Qt.DirectConnection, Q_ARG(QString, card))
#              self.parent.cardScanned(card)

    def changeParent(self, parent):
        self.parent = parent
