from zope.app.form.browser.widget import renderElement
from zope.app.form.browser.textwidgets import ASCIIWidget
from zope import component
from zope import interface
from zope import schema
from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot

from collective.googlelibraries import messageFactory as _
from collective.googlelibraries import config
from collective.googlelibraries import interfaces

class GoogleAPIKeyWidget(ASCIIWidget):
    """Google API Key widget"""

    type = 'google_api_key'

    def hasInput(self):
        return (self.name+'.url' in self.request.form and
                self.name+'.key' in self.request.form)

    def _getFormInput(self):
        url = self.request.get(self.name+'.url').strip()
        key = self.request.get(self.name+'.key').strip()
        return "%s | %s" % (url, key)

    def __call__(self):
        value = self._getFormValue()
        if value is None or value == self.context.missing_value:
            value = ''
        value = value.split("|")
        if len(value) == 2:
            value = (value[0].strip(), value[1].strip())
        else:
            value = ('', '')

        url = renderElement(self.tag,
                            type=self.type,
                            name=self.name+'.url',
                            id=self.name+'.url',
                            value=value[0],
                            cssClass=self.cssClass,
                            size=85,
                            extra=self.extra)

        key = renderElement(self.tag,
                            type=self.type,
                            name=self.name+'.key',
                            id=self.name+'.key',
                            value=value[1],
                            cssClass=self.cssClass,
                            size=85,
                            extra=self.extra)

        return "%s %s" % (url, key)


class APIKeyManager(SchemaAdapterBase):
    component.adapts(IPloneSiteRoot)
    interface.implements(interfaces.IAPIKeyManager)

    def __init__(self, context):
        super(APIKeyManager, self).__init__(context)
        properties = getToolByName(context, 'portal_properties')
        self.context = properties.google_properties

    def get_google_keys(self):
        return getattr(self.context, config.PROPERTY_GOOGLE_KEYS_FIELD, '')

    def set_google_keys(self, value):
        res = []

        for host_key in value:
            if len(host_key.split('|')) == 2:
                res.append(host_key)

        value = tuple(res)
        self.context._updateProperty(config.PROPERTY_GOOGLE_KEYS_FIELD, value)

    google_keys = property(get_google_keys, set_google_keys)

    def get_google_keys_dict(self):

        keys = self.get_google_keys()
        res = {}

        for value in keys:
            value = value.split("|")
            if len(value) == 2:
                res[value[0].strip()] = value[1].strip()

        return res

    def api_key(self, request):

        host = request.get('SERVER_URL')
        keys = self.get_google_keys()
        res = {}

        for value in keys:
            if value.startswith(host):
                value = value.split("|")
                if len(value) == 2:
                    return value[1].strip()
