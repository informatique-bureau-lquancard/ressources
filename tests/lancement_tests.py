import unittest

# import sys
# sys.path.append("/var/www/html/ressources/tests/Fonction_tarifs_dev")
# import test_Fonction_tarifs_dev

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

if __name__ == '__main__':
    unittest.main()