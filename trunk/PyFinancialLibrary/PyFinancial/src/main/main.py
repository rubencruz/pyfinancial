import sys
from PyQt4 import QtGui

if __name__ == '__main__':
    
    #Creating QT application and setting style
    app = QtGui.QApplication(sys.argv)
    QtGui.QApplication.setStyle('plastique')
    
    #Here we should initialize our calculator interface and controller
    
    #Initing application
    app.exec_()