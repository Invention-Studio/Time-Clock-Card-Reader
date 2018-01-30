from SerialReader import SerialReader
from PyQt4 import QtCore

class CardReaderThread(QtCore.QThread):
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self)
        self.parent = parent

    def run(self):
        self.reader = SerialReader("COM5")
        card = ""
        while True:
          if self.reader.isFound():
              card = self.reader.readCard()
              self.parent.cardScanned(card)

    def changeParent(self, parent):
        self.parent = parent
