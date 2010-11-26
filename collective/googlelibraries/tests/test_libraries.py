import unittest

from collective.googlelibraries import libraries

class Test(unittest.TestCase):
    
    def setUp(self):
        self.manager = libraries.LibraryManager(None)
    
    def test_libs(self):
        libraries = self.manager.libraries

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test))
    return suite
