import unittest

from collective.googlelibraries import apikey
from collective.googlelibraries.tests import base

class Test(base.TestCase):

    def afterSetUp(self):
        self.manager = apikey.APIKeyManager(self.portal)

    def test_keys(self):
        self.failUnless(len(self.manager.google_keys)==0)
        self.manager.google_keys = ('http://nohost | ZZOOPPEE',)
        self.failUnless(len(self.manager.google_keys)==1)

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test))
    return suite
