import unittest

class TestUntils(unittest.TestCase):
    
    def test1(self):
        print( self.assertTrue(False) )
        print( "KO" )

    def test2(self):
        print( self.assertTrue(True)  )
        print( "OK" )

    def test3(self):
        print( self.assertTrue(True)  )
        print( "OK" )