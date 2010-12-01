from plone.app.layout.viewlets.common import ViewletBase
from zope import component
from zope import interface

from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from collective.googlelibraries import interfaces
from collective.googlelibraries import libraries
from Products.ResourceRegistries.browser.scripts import ScriptsView
import urllib

BASE = {'inline':False,
        'conditionalcomment':'',
        'src':''}
JSAPI = BASE.copy()
JSAPI['src'] = 'https://www.google.com/jsapi?key='

class ScriptsView(ScriptsView):
    """The google libraries viewlet
    
    should render the include of jsapi with key and the google.load calls
    """

    def scripts(self):
        """The super version of this view is the one responsible to cook
        javascript resources. This version first include google libraries
        and then append the plone resources
        """

        result = []
        libs = self.library_manager.libraries
        api_key = self.api_key

        if api_key:
            data = JSAPI.copy()
            data['src'] += self.api_key
            result.append(data)

        if libs and api_key:

            for lib in libs:
                data = BASE.copy()
                data['src'] = lib.url
                result.append(data)

        result.extend(super(ScriptsView,self).scripts())

        return result

    @property
    def api_key(self):
        return self.apikey_manager.api_key(self.request)

    @property
    def apikey_manager(self):
        return interfaces.IAPIKeyManager(self.portal)

    @property
    def library_manager(self):
        return interfaces.ILibraryManager(self.portal)

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()
