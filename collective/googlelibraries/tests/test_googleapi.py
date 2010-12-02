import unittest

from collective.googlelibraries import googleapi
from collective.googlelibraries.tests import base

class TestGoogleMaps(unittest.TestCase):

    def setUp(self):
        self.maps = googleapi.MapsLibrary()
    
    def test_url(self):
        self.failUnless(self.maps.url=="http://maps.google.com/maps/api/js?sensor=false")

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGoogleMaps))
    return suite
