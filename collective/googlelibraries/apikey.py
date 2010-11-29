from zope.interface import implements
from zope.schema import ASCIILine
from zope.schema.interfaces import IASCIILine

#taken from Products.Maps

class IGoogleAPIKey(IASCIILine):
    u"""Field for a google api key."""

class GoogleAPIKey(ASCIILine):
    __doc__ = IGoogleAPIKey.__doc__
    implements(IGoogleAPIKey)
