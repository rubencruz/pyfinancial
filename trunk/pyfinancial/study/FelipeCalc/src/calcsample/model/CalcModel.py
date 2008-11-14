
class Mode(object):
    EntryMode = 1  
    SaveMode = 2

class CalcModel:
    
    def __init__(self):
        self.screen = 0
        self.xReg = 0
        self.listeners = []
        self.mode = Mode.EntryMode
    
    def pushNumber(self, num):
        if self.mode == Mode.SaveMode:
            self.screen = num
            self.mode = Mode.EntryMode
        else:
            self.screen = self.screen * 10 + num
        self.fireStateChangedEvent(self.screen)
            
    def sum(self):
        result = self.screen + self.xReg
        self._pushResult(result)
            
    def minus(self):
        result = self.screen - self.xReg
        self._pushResult(result)
            
    def mult(self):
        result = self.screen * self.xReg
        self._pushResult(result)    
        
    def div(self):
        result = self.screen / self.xReg
        self._pushResult(result)
        
    def _pushResult(self, num):
        self.xReg = num
        self.screen = num
        self.mode = Mode.SaveMode
        self.fireStateChangedEvent(num)
        
    def enterValue(self):
        self.xReg = self.screen
        self.mode = Mode.SaveMode

    def addListener(self, listener):
        self.listeners.append(listener)
        
    def fireStateChangedEvent(self, num):
        for listener in self.listeners:
            listener.stateChanged(num)
