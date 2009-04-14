from decimal import Decimal

class AmortizationTable:
    
    def __init__(self, numberOfPeriods):
        self._lines = []
        self.__numberOfPeriods = numberOfPeriods
        zero = Decimal("0")
        for i in range(0, numberOfPeriods + 1):
            self._lines.append((zero, zero, zero, zero, zero, zero))
    
    def getNumberOfPeriods(self):
        return self.__numberOfPeriods
    
    def getNumberOfLines(self):
        return len(self._lines)

    def getPayment(self, n):
        col0, col1, col2, col3, col4, col5 = self._lines[n]
        return col0
     
    def getInterest(self, n):
        col0, col1, col2, col3, col4, col5 = self._lines[n]
        return col1
        
    def getNewAcumulatedInterest(self, n):
        col0, col1, col2, col3, col4, col5 = self._lines[n]
        return col2
        
    def getAmortization(self, n):
        col0, col1, col2, col3, col4, col5 = self._lines[n]
        return col3

    def getNewAcumulatedAmortization(self, n):
        col0, col1, col2, col3, col4, col5 = self._lines[n]
        return col4

    def getNewAmountToBePayed(self, n):
        col0, col1, col2, col3, col4, col5 = self._lines[n]
        return col5

    def setTableLine(self, n, payment, interest, acumulatedInterest, amortization, newAcumulatedAmortization, newAmountToBePayed):
        self._lines[n] = (payment, interest, acumulatedInterest, amortization, newAcumulatedAmortization, newAmountToBePayed)

    def setPayment(self, n, newValue):
        col0, col1, col2, col3, col4, col5 = self._lines[n]
        self._lines[n] = (newValue, col1, col2, col3, col4, col5) 
     
    def setInterest(self, n, newValue):
        col0, col1, col2, col3, col4, col5 = self._lines[n]
        self._lines[n] = (col0, newValue, col2, col3, col4, col5) 
        
    def setNewAcumulatedInterest(self, n, newValue):
        col0, col1, col2, col3, col4, col5 = self._lines[n]
        self._lines[n] = (col0, col1, newValue, col3, col4, col5) 
        
    def setAmortization(self, n, newValue):
        col0, col1, col2, col3, col4, col5 = self._lines[n]
        self._lines[n] = (col0, col1, col2, newValue, col4, col5) 

    def setNewAcumulatedAmortization(self, n, newValue):
        col0, col1, col2, col3, col4, col5 = self._lines[n]
        self._lines[n] = (col0, col1, col2, col3, newValue, col5) 

    def setNewAmountToBePayed(self, n, newValue):
        col0, col1, col2, col3, col4, col5 = self._lines[n]
        self._lines[n] = (col0, col1, col2, col3, col4, newValue)
        
        
         