from zope import interface
from zope import schema

from collective.googlelibraries import messageFactory as _

class IGoogleLibrariesLayer(interface.Interface):
    """Browser layer"""

class ILibrary(interface.Interface):
    """ """
    id = schema.ASCIILine(title=_("label_id",default=u"id"))

    title = schema.TextLine(title=_("label_title",default=u"Title"))

    version = schema.ASCIILine(title=_("label_version", default=u"Version"))

    url = schema.URI(title=_("label_url",default=u"URL minified"))
    
    optionalSettings = schema.Dict(title=_("label_optionalSettings",
                                           default=u"Optional settings"))

    def settings_schema(self):
        """Return schema associated to the optionSettings"""

class ILibraryField(schema.interfaces.IASCIILine):
    u"""Field for Library"""

class LibraryField(schema.ASCIILine):
    __doc__ = ILibraryField.__doc__
    interface.implements(ILibraryField)

class LibrarySettingSchema(interface.Interface):
    """Library can support settings. Settings are complex data structure
    """

    minified = schema.Bool(title=_("label_minified", default=u"Minified"))

class ILibraryManager(interface.Interface):
    """The library manager. manage CRUD on Library"""

    libraries = schema.Tuple(
                    title=_('label_libraries',
                            default=u'Google Libraries'),
                    description=_('help_libraires',
                                  default=u"Add Google Libraries."),
                    unique=True,
                    value_type=LibraryField(
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

    def api_key(request):
        """Return the key associated to the host. The host is extracted
        from the request object"""
