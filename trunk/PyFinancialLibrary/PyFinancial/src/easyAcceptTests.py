from pythoneasyaccept.PythonEasyAcceptFacade import PythonEasyAcceptFacade
from main.facade import *
from calcElements.model import *

class Tests:

    #Put the US1 test script file into the "testScripts" array
    userStory1 = "../tests/US1.txt"
    testScripts = [userStory1]

    #Instantiate your software facade
    model = Model()
    myFacade = calcController(model)

    #Instantiate PythonEasyAcceptFacade
    pythonEAFacade = PythonEasyAcceptFacade(myFacade, testScripts)

    #Execute the tests
    pythonEAFacade.executeTests()

    #Print the tests execution results
    print pythonEAFacade.getCompleteResults()