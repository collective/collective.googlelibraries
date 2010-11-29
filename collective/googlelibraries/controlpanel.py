from zope import component
from zope import schema
from zope import interface
from zope.formlib.form import FormFields

from plone.app.controlpanel.form import ControlPanelForm
from plone.fieldsets.fieldsets import FormFieldsets
from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFPlone.interfaces import IPloneSiteRoot

from collective.googlelibraries import messageFactory as _
from collective.googlelibraries import config
from collective.googlelibraries import apikey

DEFAULT_LOADER_MODE_CHOICES = schema.vocabulary.SimpleVocabulary((
      schema.vocabulary.SimpleTerm('loader','loader',_(u'google.load')),
      schema.vocabulary.SimpleTerm('scripttag','scripttag',_(u'script tags')),
      schema.vocabulary.SimpleTerm('onerequest','onerequest',_(u'One request')),
))

class IFormSchema(interface.Interface):

    google_keys = schema.Tuple(
                    title=_('label_google_keys',
                            default=u'Google Libraries API Keys'),
                    description=_('help_google_keys',
                                  default=u"Add Google Libraries API keys. "
                                           "You have to use the client "
                                           "side url at which your site "
                                           "is visible."),
                    unique=True,
                    value_type=apikey.GoogleAPIKey(
                        title=_('Key'),
                    ),
                  )

    loader_mode = schema.Choice(
                           title=_('label_loader_mode', default=u'Mode'),
                           description=_('help_loader_mode',
                                         default=u"Include mode used to include"
                                         "libraries"),
                           vocabulary=DEFAULT_LOADER_MODE_CHOICES)

class FormAdapter(SchemaAdapterBase):
    component.adapts(IPloneSiteRoot)
    interface.implements(IFormSchema)

    def __init__(self, context):
        super(FormAdapter, self).__init__(context)
        properties = getToolByName(context, 'portal_properties')
        self.context = properties.google_properties

    def get_google_keys(self):
        return getattr(self.context, config.PROPERTY_GOOGLE_KEYS_FIELD, '')

    def set_google_keys(self, value):
        self.context._updateProperty(config.PROPERTY_GOOGLE_KEYS_FIELD, value)

    google_keys = property(get_google_keys, set_google_keys)

    def get_loader_mode(self):
        return getattr(self.context, config.PROPERTY_LOADER_MODE_FIELD, '')

    def set_loader_mode(self, value):
        self.context._updateProperty(config.PROPERTY_LOADER_MODE_FIELD, value)

    loader_mode = property(get_loader_mode, set_loader_mode)

class GoogleLibrariesControlPanel(ControlPanelForm):
    """Control panel for c.googlelibraries. 
    
    Feature:
    * setup api key for each domain
    * choose what to libraries to load / include
    * choose include mode
    """

    form_fields = FormFields(IFormSchema)
    label = _("GoogleLibraries settings")
    description = None
    form_name = _("GoogleLibraries settings")

    def _on_save(self, data):
        pass
