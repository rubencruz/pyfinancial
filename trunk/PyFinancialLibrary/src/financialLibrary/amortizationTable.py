from decimal import Decimal

class AmortizationTable:
    """ Represents an amortization table.
    """

    
    def __init__(self, numberOfPeriods):
        """ Constructor for the AmortizationTable class.

        @param numberOfPeriods: amortization periods number
        @type numberOfPeriods: int
        """
        
        self._lines = []
        self.__numberOfPeriods = numberOfPeriods
        zero = Decimal("0")
        for i in range(0, numberOfPeriods + 1):
            self._lines.append((zero, zero, zero, zero, zero, zero))
    
    def getNumberOfPeriods(self):
        return self.__numberOfPeriods
    
    def getNumberOfLines(self):
        """ Return the number of lines. The number of lines is the
        number of periods plus one.

        @return: numberOfLines
        @rtype: int
        """        
        return len(self._lines)

    def getPayment(self, lineNumber):
        col0, col1, col2, col3, col4, col5 = self._lines[lineNumber]
        return col0
     
    def getInterest(self, lineNumber):
        col0, col1, col2, col3, col4, col5 = self._lines[lineNumber]
        return col1
        
    def getNewAcumulatedInterest(self, lineNumber):
        col0, col1, col2, col3, col4, col5 = self._lines[lineNumber]
        return col2
        
    def getAmortization(self, lineNumber):
        col0, col1, col2, col3, col4, col5 = self._lines[lineNumber]
        return col3

    def getNewAcumulatedAmortization(self, lineNumber):
        col0, col1, col2, col3, col4, col5 = self._lines[lineNumber]
        return col4

    def getNewAmountToBePayed(self, lineNumber):
        col0, col1, col2, col3, col4, col5 = self._lines[lineNumber]
        return col5

    def setTableLine(self, lineNumber, payment, interest, acumulatedInterest, amortization, newAcumulatedAmortization, newAmountToBePayed):
        """ Set a specific line of the table.
        """                
        self._lines[lineNumber] = (payment, interest, acumulatedInterest, amortization, newAcumulatedAmortization, newAmountToBePayed)

    def setPayment(self, lineNumber, newValue):
        col0, col1, col2, col3, col4, col5 = self._lines[lineNumber]
        self._lines[lineNumber] = (newValue, col1, col2, col3, col4, col5) 
     
    def setInterest(self, lineNumber, newValue):
        col0, col1, col2, col3, col4, col5 = self._lines[lineNumber]
        self._lines[lineNumber] = (col0, newValue, col2, col3, col4, col5) 
        
    def setNewAcumulatedInterest(self, lineNumber, newValue):
        col0, col1, col2, col3, col4, col5 = self._lines[lineNumber]
        self._lines[lineNumber] = (col0, col1, newValue, col3, col4, col5) 
        
    def setAmortization(self, lineNumber, newValue):
        col0, col1, col2, col3, col4, col5 = self._lines[lineNumber]
        self._lines[lineNumber] = (col0, col1, col2, newValue, col4, col5) 

    def setNewAcumulatedAmortization(self, lineNumber, newValue):
        col0, col1, col2, col3, col4, col5 = self._lines[lineNumber]
        self._lines[lineNumber] = (col0, col1, col2, col3, newValue, col5) 

    def setNewAmountToBePayed(self, lineNumber, newValue):
        col0, col1, col2, col3, col4, col5 = self._lines[lineNumber]
        self._lines[lineNumber] = (col0, col1, col2, col3, col4, newValue)
         