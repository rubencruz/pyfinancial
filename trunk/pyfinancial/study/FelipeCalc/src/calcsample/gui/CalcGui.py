#!/usr/bin/python

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from calcsample.controller import CalcController
from calcsample.model import CalcModel
from calcsample.gui import CalcButton


class CalcGui(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.controller = None

        self.setWindowTitle('CalcSample')
        
        self.screen = QtGui.QLineEdit()
        self.screen.setReadOnly(True)
        self.screen.setAlignment(QtCore.Qt.AlignRight)
        self.screen.setText("0")

        grid = QtGui.QGridLayout()
        
        self._addGridButton(grid, "7", 0, 0)
        self._addGridButton(grid, "8", 0, 1)
        self._addGridButton(grid, "9", 0, 2)
        self._addGridButton(grid, "/", 0, 3)
        self._addGridButton(grid, "4", 1, 0)
        self._addGridButton(grid, "5", 1, 1)
        self._addGridButton(grid, "6", 1, 2)
        self._addGridButton(grid, "x", 1, 3)
        self._addGridButton(grid, "3", 2, 0)
        self._addGridButton(grid, "2", 2, 1)
        self._addGridButton(grid, "1", 2, 2)
        self._addGridButton(grid, "-", 2, 3)
        self._addGridButton(grid, "0", 3, 1)
        self._addGridButton(grid, "ENT", 3, 2)
        self._addGridButton(grid, "+", 3, 3)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.screen)
        vbox.addLayout(grid)

        self.setLayout(vbox)

    def _addGridButton(self, gridLayout, text, x, y):        
        button = CalcButton.CalcButton(text)
        self.connect(button, QtCore.SIGNAL('activated(QString &)'), self.buttonClicked)
        gridLayout.addWidget(button, x, y)
        
    def buttonClicked(self, text):
        if text == "ENT":
            self.controller.enterValue()
        elif text == "+":
            self.controller.sum()
        elif text == "-":
            self.controller.minus()
        elif text == "x":
            self.controller.mult()
        elif text == "/":
            self.controller.div()
        else:
            self.controller.pushNumber(int(text))
        
    def setController(self, controller):
        self.controller = controller
        
    def stateChanged(self, value):
        self.screen.setText(str(value))
