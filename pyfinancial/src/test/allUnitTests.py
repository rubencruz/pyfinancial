import unittest
from unit.libraryTests import *

if __name__ == "__main__":
    suite1 = unittest.makeSuite(LibraryTestCase, "test")
    
    runner = unittest.TextTestRunner()
    runner.run(suite1)