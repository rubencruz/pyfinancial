from PyQt4 import QtCore, QtGui

class CalcButton(QtGui.QPushButton):
    def __init__(self, text, parent=None):
        QtGui.QPushButton.__init__(self, text, parent)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.connect(self, QtCore.SIGNAL('clicked()'), self.clickEvent)

    def clickEvent(self):
        self.emit(QtCore.SIGNAL('activated(QString &)'), self.text())