from calcsample.model import CalcModel

class CalcController:
    
    def __init__(self, model=None):
        self.model = model
    
    def pushNumber(self, num):
        self.model.pushNumber(num)
            
    def sum(self):
        self.model.sum()
    
    def minus(self):
        self.model.minus()
    
    def mult(self):
        self.model.mult()
    
    def div(self):
        self.model.div()
        
    def enterValue(self):
        self.model.enterValue()
