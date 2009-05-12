def invDiv(self):
        if self.__isGPushed or self.__isFPushed:
            self.__fireException("Function not yet implemented.")
            self.__deactiveFandG()
        else:
            # "inv /"
            try:
                result = self.__calcStack.getXReg() / self.__calcStack.getYReg()
                self.__calcStack.rollCounterClockWise()
                self.__calcStack[0] = result
                self.__calcStack[3] = self.__calcStack[2]
        
                self.mode = Mode.OperationMode
                self.base = None
                self.dotActived = False
        
                self.__fireStackRegisters(self.getAllStackRegisters())
                self.__fireScreenChangedEvent()
                 
            except Exception, e:
                self.__fireException(e.message)
