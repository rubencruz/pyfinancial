import unittest
from financialLibrary.amortizationTable import *
from decimal import Decimal

class AmortizationTableTestCase (unittest.TestCase):
    
    def testAmortizationTable(self):
        table = AmortizationTable(6)
        self.assertEquals(6, table.getNumberOfPeriods())
        self.assertEquals(7, table.getNumberOfLines())
        
        for n in range(0, table.getNumberOfLines()):
            self.assertEquals(Decimal("0"), table.getAmortization(n))
            self.assertEquals(Decimal("0"), table.getInterest(n))
            self.assertEquals(Decimal("0"), table.getPayment(n))
            self.assertEquals(Decimal("0"), table.getNewAcumulatedAmortization(n))
            self.assertEquals(Decimal("0"), table.getNewAcumulatedInterest(n))
            self.assertEquals(Decimal("0"), table.getNewAmountToBePayed(n))
            
        table.setAmortization(0, Decimal("1"))
        table.setInterest(1, Decimal("2"))
        table.setPayment(2, Decimal("3"))
        table.setNewAcumulatedAmortization(3, Decimal("4"))
        table.setNewAcumulatedInterest(4, Decimal("5"))
        table.setNewAmountToBePayed(5, Decimal("6"))
        table.setNewAmountToBePayed(6, Decimal("7"))
        
        self.assertEquals(Decimal("1"), table.getAmortization(0))
        for n in range(1, table.getNumberOfLines()):
            self.assertEquals(Decimal("0"), table.getAmortization(n))
        
        self.assertEquals(Decimal("0"), table.getInterest(0))
        self.assertEquals(Decimal("2"), table.getInterest(1))
        for n in range(2, table.getNumberOfLines()):
            self.assertEquals(Decimal("0"), table.getInterest(n))
        
        self.assertEquals(Decimal("3"), table.getPayment(2))
        for n in range(0, 2):
            self.assertEquals(Decimal("0"), table.getPayment(n))
        for n in range(3, table.getNumberOfLines()):
            self.assertEquals(Decimal("0"), table.getPayment(n))
                    
        self.assertEquals(Decimal("4"), table.getNewAcumulatedAmortization(3))
        for n in range(0, 3):
            self.assertEquals(Decimal("0"), table.getNewAcumulatedAmortization(n))
        for n in range(4, table.getNumberOfLines()):
            self.assertEquals(Decimal("0"), table.getNewAcumulatedAmortization(n))
        
        self.assertEquals(Decimal("5"), table.getNewAcumulatedInterest(4))
        for n in range(0, 4):
            self.assertEquals(Decimal("0"), table.getNewAcumulatedInterest(n))
        for n in range(5, table.getNumberOfLines()):
            self.assertEquals(Decimal("0"), table.getNewAcumulatedInterest(n))
        
        self.assertEquals(Decimal("6"), table.getNewAmountToBePayed(5))
        for n in range(0, 5):
            self.assertEquals(Decimal("0"), table.getNewAmountToBePayed(n))                        
        self.assertEquals(Decimal("7"), table.getNewAmountToBePayed(6))        