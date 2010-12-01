import unittest

from collective.googlelibraries import libraries
from collective.googlelibraries.tests import base

class TestLibraryManager(base.TestCase):

    def afterSetUp(self):
        self.manager = libraries.LibraryManager(self.portal)

    def test_get_libraries_after_setup(self):
        self.failUnless(len(self.manager.libraries)==0)

    def test_get_libraries(self):
        self.manager.libraries = ('jquery | 1.4.2',)
        self.failUnless(len(self.manager.libraries)==1)
        lib, = self.manager.libraries
        self.failUnless(type(lib)==libraries.Library)

    def test_set_libraries_onlyname(self):
        self.manager.libraries = ('jquery',)
        lib, = self.manager.libraries
        self.failUnless(lib.version == '1.4.4')
        self.failUnless(lib.version == lib.versions[-1])
    
    def test_set_libraries_libandversion(self):
        self.manager.libraries = ('jquery | 1.4.4',)
        self.failUnless(len(self.manager.libraries)==1)

    def test_set_libraries_notexistinglib(self):
        self.manager.libraries = ('notexisting',)
        self.failUnless(len(self.manager.libraries)==0)

    def test_set_libraries_badversion(self):
        self.manager.libraries = ('jquery | 1.1',)
        self.failUnless(len(self.manager.libraries)==0)

    def test_set_libraries_badconfigformat(self):
        self.manager.libraries = 'bad format not a tuple'
        self.failUnless(len(self.manager.libraries)==0)

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.lib = libraries.Library('jquery')
        self.lib.version = '1.4.4'

    def test_url(self):
        self.failUnless(self.lib.url) == "https://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js"

    def test_version(self):
        self.lib._version = ''
        self.lib.version == self.lib.versions[-1]

    def test_optionalSettings(self):
        self.lib.version = '2'
        self.lib.optionalSettings = {"uncompressed" : True, "wrongkey":"care?"}
        settings = self.lib.optionalSettings
        self.failUnless(settings.get('wrongkey',None) is None)
        self.failUnless(settings.get('uncompressed') == True)
    
    def test_tostring(self):
        tostring = str(self.lib)
        self.failUnless(tostring == 'jquery | 1.4.4 | ', tostring)

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestLibraryManager))
    suite.addTest(unittest.makeSuite(TestLibrary))
    return suite
