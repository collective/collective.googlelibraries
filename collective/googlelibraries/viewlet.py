from plone.app.layout.viewlets.common import ViewletBase
from zope import component
from zope import interface

from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from collective.googlelibraries import interfaces
from collective.googlelibraries import libraries

TEMPLATES={
       'jsapi':"""<script type="text/javascript" src="https://www.google.com/jsapi?key=%(KEY)s"></script>""",
       'script':"""<script src="%(url_min)s"><script> """,
       'load':"""google.load("%(id)s","%(version)s",{uncompressed:false})""",
           }
DEBUG = True
if DEBUG:
    TEMPLATES['scripttag'] = """<script src="%(url)s"><script> """
    TEMPLATES['load']   = """google.load("%(id)s","%(version)s",{uncompressed:true})"""

class GoogleLibrariesViewlet(ViewletBase):
    """The google libraries viewlet
    
    should render the include of jsapi with key and the google.load calls
    """
    interface.implements(interfaces.IGoogleLibrariesViewlet)

    template_scripttags = ViewPageTemplateFile('templates/scripttags.pt')
    template_load       = ViewPageTemplateFile('templates/load.pt')
    template_onerequest = ViewPageTemplateFile('templates/onerequest.pt')

    @property
    def libraries(self):
        res = []
        libs = self.library_manager.libraries_dict
        if self.mode == 'scripttag':
            #return a list of URL
            for lib in libs.keys():
                res.append(libs[lib].url)
        self.context.plone_log(res)
        return res

    @property
    def mode(self):
        return self.library_manager.loader_mode

    @property
    def api_key(self):
        google_keys = self.apikey_manager.get_google_keys_dict()
        host = self.request.get('SERVER_URL')
        return google_keys.get(host, '')

    def index(self):
        if self.mode == 'scripttag':
            return self.template_scripttags()

        elif self.mode == 'googleload':
            return self.template_load()
        else:
            return self.template_onerequest()

    @property
    def apikey_manager(self):
        return interfaces.IAPIKeyManager(self.portal)

    @property
    def library_manager(self):
        return interfaces.ILibraryManager(self.portal)

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()
