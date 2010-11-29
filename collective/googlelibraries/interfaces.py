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

DEFAULT_LOADER_MODE_CHOICES = schema.vocabulary.SimpleVocabulary((
    schema.vocabulary.SimpleTerm('loader','loader',_(u'google.load')),
    schema.vocabulary.SimpleTerm('scripttag','scripttag',_(u'script tags')),
    schema.vocabulary.SimpleTerm('onerequest','onerequest',_(u'One request')),
))

class ILibraryManager(interface.Interface):
    """The library manager. manage CRUD on Library"""


    loader_mode = schema.Choice(
                       title=_('label_loader_mode', default=u'Mode'),
                       description=_('help_loader_mode',
                                     default=u"Include mode used to include"
                                     "libraries"),
                       vocabulary=DEFAULT_LOADER_MODE_CHOICES)

    libraries = schema.Tuple(
                    title=_('label_libraries',
                            default=u'Google Libraries'),
                    description=_('help_libraires',
                                  default=u"Add Google Libraries"),
                    unique=True,
                    value_type=schema.ASCIILine(
                        title=_('Library'),
                    ),
                  )


class IGoogleAPIKey(schema.interfaces.IASCIILine):
    u"""Field for a google api key."""

class GoogleAPIKey(schema.ASCIILine):
    __doc__ = IGoogleAPIKey.__doc__
    interface.implements(IGoogleAPIKey)


class IAPIKeyManager(interface.Interface):

    google_keys = schema.Tuple(
                    title=_('label_google_keys',
                            default=u'Google Libraries API Keys'),
                    description=_('help_google_keys',
                                  default=u"Add Google Libraries API keys. "
                                           "You have to use the client "
                                           "side url at which your site "
                                           "is visible."),
                    unique=True,
                    value_type=GoogleAPIKey(
                        title=_('Key'),
                    ),
                  )
