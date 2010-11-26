import unittest

class Test(unittest.TestCase):
    
    def test_libs(self):
        self.failUnless(1 == 1)

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test))
    return suite
