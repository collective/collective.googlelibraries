import unittest

from collective.googlelibraries import scripts
from collective.googlelibraries.tests import base

class Test(base.TestCase):

    def afterSetUp(self):
        self.view = scripts.ScriptsView(self.portal, self.portal.REQUEST)

    def test_scripts(self):
        scripts = self.view.scripts()
        srcs = [script['src'] for script in scripts]
        for src in srcs:
            self.failUnless('jsapi' not in src)

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test))
    return suite
