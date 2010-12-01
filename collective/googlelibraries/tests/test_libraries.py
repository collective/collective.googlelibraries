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
        lib, = self.manager.libraries
        self.failUnless(type(lib)==libraries.Library)

    def test_noversion(self):
        self.manager.libraries = ('jquery | ',)
        lib, = self.manager.libraries
        self.failUnless(lib.version == lib.versions[-1])

    def test_notexistinglib(self):
        self.manager.libraries = ('notexisting | ',)
        self.failUnless(len(self.manager.libraries)==0)

    def test_badversion(self):
        self.manager.libraries = ('jquery | 1.1',)
        self.failUnless(len(self.manager.libraries)==0)

    def test_badconfigformat(self):
        self.manager.libraries = 'bad format'
        self.failUnless(len(self.manager.libraries)==0)

    def test_optionalSettings(self):
        lib = libraries.Library("maps", "Google Maps", '2', '', '')
        lib.optionalSettings = {"callback" : "mapsLoaded", "wrongkey":"care?"}
        settings = lib.optionalSettings
        self.failUnless(settings.get('wrongkey',None) is None)
        self.failUnless(settings.get('callback') == "mapsLoaded")

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test))
    return suite
