from plone.app.layout.viewlets.common import ViewletBase
from zope import interface

from collective.googlelibraries import interfaces
from collective.googlelibraries import libraries

class GoogleLibraries(ViewletBase):
    """The google libraries viewlet
    
    should render the include of jsapi with key and the google.load calls
    """
    interface.implements(interfaces.IGoogleLibraries)
    
    def libraries(self):
        return []

