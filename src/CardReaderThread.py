from SerialReader import SerialReader

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
              self.parent.cardScanned(card)
