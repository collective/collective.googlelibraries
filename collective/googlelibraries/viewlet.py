from plone.app.layout.viewlets.common import ViewletBase
from zope import interface

from collective.googlelibraries import interfaces
from collective.googlelibraries import libraries

TEMPLATES={
       'jsapi':"""<script type="text/javascript" src="https://www.google.com/jsapi?key=%(KEY)s"></script>""",
       'script':"""<script src="%(url_min)s"><script> """,
       'load':"""google.load("%(id)s","%(version)s",{uncompressed:false})""",
           }
DEBUG = True
if DEBUG:
    TEMPLATES['script'] = """<script src="%(url)s"><script> """
    TEMPLATES['load']   = """google.load("%(id)s","%(version)s",{uncompressed:true})"""

class GoogleLibrariesViewlet(ViewletBase):
    """The google libraries viewlet
    
    should render the include of jsapi with key and the google.load calls
    """
    interface.implements(interfaces.IGoogleLibrariesViewlet)
    
    @properties
    def libraries(self):
        return []

    @property
    def mode(self):
        return 'script'

    def render_libraries(self):
        s = TEMPLATES['jsapi']
        for l in libraries():
            s += TEMPLATES[self.mode]%(l)
        return s
