import unittest

from collective.googlelibraries import libraries
from collective.googlelibraries.tests import base

class Test(base.TestCase):

    def afterSetUp(self):
        self.manager = libraries.LibraryManager(self.portal)

    def test_libraries(self):
        self.failUnless(len(self.manager.libraries)==0)
        self.manager.libraries = ('jquery | 1.4.2',)
        self.failUnless(len(self.manager.libraries)==1)

    def test_loader_mode(self):
        self.failUnless(not self.manager.loader_mode)
        self.manager.loader_mode = 'autoload'

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test))
    return suite
