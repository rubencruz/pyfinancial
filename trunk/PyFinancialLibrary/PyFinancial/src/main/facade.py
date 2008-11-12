#****************************************************************************
# facade.py, This module represents the facade of our RPN calculator visor, that is
#responsible for connecting the BL with GUI 
#
# pyFinancial, a financial library for python users
# Copyright (C) 2008, Felipe Leal, David Candeia, Everton Leandro and Diego Dantas
#
# This is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License, either Version 2 or any later
# version.  This program is distributed in the hope that it will be useful,
# but WITTHOUT ANY WARRANTY.  See the included LICENSE file for details.
#*****************************************************************************

class calcController:
    """ This class represents the controller of our calculator that is responsible
    for receiving events from the interface and then requesting services from the BL """
    
    def __init__(self, model=None):
        self.model = model
    
    def pushNumber(self, num):
        """ Entering a number from the interface into the visor """
        self.model.pushNumber(num)
    
    def getXReg(self):
        """ Requesting the value of the X register """
        self.model.getXReg()
    
    def getYReg(self):
        """ Requesting the value of the Y register """
        self.model.getYReg()
        
    def getWReg(self):
        """ Requesting the value of the W register """
        self.model.getWReg()
        
    def getZReg(self):
        """ Requesting the value of the Z register """
        self.model.getZReg()   
        
    def rollClockWise(self):
        """ Requesting that the registers roll starting from X into Z """
        self.model.rollClockWise()
    
    def rollCounterClockWise(self):
        """ Requesting that the registers roll starting from Z into X """
        self.model.rollCounterClockWise()                 
            
    def sum(self):
        """ Requesting the sum operation between the values in the X 
        register and the Y register """
        self.model.sum()
    
    def minus(self):
        """ Requesting the minus operation between the values in the X 
        register and the Y register """
        self.model.minus()
    
    def mult(self):
        """ Requesting the multiplication operation between the values in the X 
        register and the Y register """
        self.model.mult()
    
    def div(self):
        """ Requesting the division operation between the values in the X 
        register and the Y register """
        self.model.div()
        
    def enterValue(self):
        """ Requesting that the value placed at X be stored in the Y register  """
        self.model.enterValue()