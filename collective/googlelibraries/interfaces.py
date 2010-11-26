from zope import interface
from zope import schema

class IGoogleLibrariesLayer(interface.Interface):
    """Browser layer"""

class ILibrary(interface.Interface):
    """ """
    id = schema
    
    title = schema
    
    version = schema

class ILibraryManager(interface.Interface):
    """Define API to manage libraries"""

    def libraries():
        """Accessor. Return a list of libraries to load"""

    def available_libraries():
        """Return the list of available libraries"""

    def add(library):
        """Add a library to load"""

    def remove(library):
        """Remove a library from loading"""
