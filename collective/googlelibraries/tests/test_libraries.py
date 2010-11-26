import unittest

from collective.googlelibraries import libraries

class TestLibraryManager(unittest.TestCase):

    def setUp(self):
        self.manager = libraries.LibraryManager(None)
        self.jquery = libraries.GOOGLE_LIBRARIES["jquery"]["1.4.4"]

    def test_add(self):
        libraries = self.manager.libraries
        self.failUnless(len(libraries)==0)
        self.manager.add(self.library)
        self.failUnless(len(libraries)==1)

    def test_remove(self):
        libraries = self.manager.libraries
        self.manager.add(libraries.GOOGLE_LIBRARIES[0])
        self.manager.add(libraries.GOOGLE_LIBRARIES[0])

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestLibraryManager))
    return suite
