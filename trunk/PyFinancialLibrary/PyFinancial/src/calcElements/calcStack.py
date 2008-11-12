#****************************************************************************
# visorStack.py, This module represents the stack of our RPN calculator visor, that contains
#four registers called, in the sequence of storage: X, Y, Z and W.
#
# pyFinancial, a financial library for python users
# Copyright (C) 2008, Felipe Leal, David Candeia, Everton Leandro and Diego Dantas
#
# This is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License, either Version 2 or any later
# version.  This program is distributed in the hope that it will be useful,
# but WITTHOUT ANY WARRANTY.  See the included LICENSE file for details.
#*****************************************************************************


class calcStack(list):
    """ The stack used while operating numbers using the enter key. This stack contains 
    four numbers called, in the storage sequence: X, Y, Z and W. """
    
    def __init__(self, initList=None):
        if initList != None and initList and len(initList) == 4:
            list.__init__(self, initList)
        else:
            list.__init__(self, [0.0, 0.0, 0.0, 0.0])
    
    def replaceAll(self, newStack):
        """Replace stack with a new stack"""
        if newStack == None or not newStack or len(newStack) != 4:
            print "Invalid new stack "+str(newStack)
            return
        
        self[:] = newStack        
    
    def exchangeXAndY(self):
        """ Exchange X and Y positions in the stack """
        num = self[0]
        del self[0]
        self.insert(1, num)
    
    def rollCounterClockWise(self):
        """Roll stack so that X receives Y, Y receives Z, Z receives W
        and W receives X previous value"""
        num = self[0]
        del self[0]
        self.append(num)

    def rollClockWise(self):
        """Roll stack so that W receives Z, Z receives Y, Y receives X
        and X receives W previous value"""
        num = self[3]
        del self[3]
        self.insert(0, num)    
            