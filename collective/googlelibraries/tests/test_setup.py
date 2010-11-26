import unittest
from collective.googlelibraries.tests import base

class TestSetup(base.TestCase):
    
    def test_layer(self):
        self.failUnless(1 == 1)

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
