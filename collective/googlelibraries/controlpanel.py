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
from collective.googlelibraries import libraries
from collective.googlelibraries import interfaces

class GoogleLibrariesControlPanel(ControlPanelForm):
    """Control panel for c.googlelibraries. 
    
    Feature:
    * setup api key for each domain
    * choose what to libraries to load / include
    * choose include mode
    """
    
    form_fields = FormFields(interfaces.IAPIKeyManager,
                             interfaces.ILibraryManager)

    label = _("GoogleLibraries settings")
    description = None
    form_name = _("GoogleLibraries settings")

    def _on_save(self, data):
        pass
