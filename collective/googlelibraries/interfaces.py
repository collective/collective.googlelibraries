from zope import interface
from zope import schema

from collective.googlelibraries import messageFactory as _

class IGoogleLibrariesLayer(interface.Interface):
    """Browser layer"""

class ILibrary(interface.Interface):
    """ """
    id = schema.ASCIILine(title=_(u"id"))

    title = schema.TextLine(title=_(u"Title"))

    version = schema.ASCIILine(title=_(u"Version"))

    url = schema.URI(title=_(u"URL minified"))

class IGoogleLibrariesViewlet(interface.Interface):
    """An accessor component to libraries"""

    mode = schema.ASCIILine(title=_(u"Mode"),
                            description=_(u"Shoud be in 'script', 'load'"))

    libraries = schema.List(title=_(u"Libraries"),
                            value_type=schema.Object(ILibrary, title=u"Library"))


class ILibraryManager(interface.Interface):
    """Define API to manage libraries"""

    mode = schema.ASCIILine(title=_(u"Mode"),
                            description=_(u"Shoud be in 'script', 'load'"))

    libraries = schema.List(title=_(u"Libraries"),
                            value_type=schema.Object(ILibrary, title=u"Library"))

    available_libraries = schema.List(title=_(u"Libraries"),
                                      value_type=schema.Object(ILibrary, title=u"Library"))

    def add(library):
        """Add a library to load"""

    def remove(library):
        """Remove a library from loading"""
