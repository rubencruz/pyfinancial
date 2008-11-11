#!/usr/bin/python

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from calcsample.controller import CalcController
from calcsample.model import CalcModel
from calcsample.gui import CalcGui

class CalcApp:
    
    def __init__(self):
        self.app = QtGui.QApplication(sys.argv)
        model = CalcModel.CalcModel()
        controller = CalcController.CalcController(model)
        self.gui = CalcGui.CalcGui()
        self.gui.setController(controller)
        model.addListener(self.gui)
        
    def run(self):
        self.gui.show()
        sys.exit(self.app.exec_())