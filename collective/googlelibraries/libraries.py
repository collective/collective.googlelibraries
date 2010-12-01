from zope import component
from zope import interface
from zope import schema
from zope.app.form.browser.textwidgets import ASCIIWidget
from zope.app.form.browser.widget import renderElement
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot

from collective.googlelibraries import config
from collective.googlelibraries import interfaces
from collective.googlelibraries import messageFactory as _

class Library(object):
    interface.implements(interfaces.ILibrary)
    def __init__(self, id, title, versions, url_u, url, version=''):
        self.id = id
        self.title = title
        self.versions = versions
        self._version = version
        self._url = url
        self._url_u = url_u
        self.minified = True
        self._optionalSettings = {}

    @property
    def url(self):
        base = self._url
        if not self.minified:
            base = self._url_u

        return base%({'version':self.version})

    def get_version(self):
        if not self._version:
            return self.versions[-1]
        return self._version

    def set_version(self, value):
        if value in self.versions:
            self._version = value

    version = property(get_version, set_version)

    def __str__(self):
        return '%s | %s'%(self.id, self.version)

    def get_optionalSettings(self):
        return self._optionalSettings

    def set_optionalSettings(self, value):
        if type(value) != dict:
            return
        for k in value.keys():
            if k not in config.OPTIONAL_SETTINGS_KEYS:
                continue
            self._optionalSettings[k] = value[k]

    optionalSettings = property(get_optionalSettings, set_optionalSettings)

#Now lets define all available libraries

GOOGLE_LIBRARIES = {}

v = ('1.0.0', '1.0.1', '1.0.2')
url = "https://ajax.googleapis.com/ajax/libs/chrome-frame/%(version)s/CFInstall.min.js"
url_u = "https://ajax.googleapis.com/ajax/libs/chrome-frame/%(version)s/CFInstall.js"
lib = Library("chrome-frame", "Chrome Frame", v, url_u, url)
GOOGLE_LIBRARIES["chrome-frame"] = lib

v = ('1.1.1',
          '1.2.0', '1.2.3',
          '1.3.0', '1.3.1', '1.3.2',
          '1.4.0', '1.4.1', '1.4.3',
          '1.5')
url_u = "https://ajax.googleapis.com/ajax/libs/dojo/%(version)s/dojo/dojo.xd.js.uncompressed.js"
url = "https://ajax.googleapis.com/ajax/libs/dojo/%(version)s/dojo/dojo.xd.js"
lib = Library("dojo","Dojo", v, url_u, url)
GOOGLE_LIBRARIES["dojo"] = lib

v = ('3.0.0','3.1.0')
url_u = "https://ajax.googleapis.com/ajax/libs/ext-core/%(version)s/ext-core-debug.js"
url = "https://ajax.googleapis.com/ajax/libs/ext-core/%(version)s/ext-core.js"
lib = Library("ext-core","Ext Core", v, url_u, url)

GOOGLE_LIBRARIES["ext-core"] = lib

v = ('1.2.3', '1.2.6',
     '1.3.0', '1.3.1', '1.3.2',
     '1.4.0', '1.4.1', '1.4.2','1.4.3','1.4.4')
url_u = "https://ajax.googleapis.com/ajax/libs/jquery/%(version)s/jquery.js"
url = "https://ajax.googleapis.com/ajax/libs/jquery/%(version)s/jquery.min.js"
GOOGLE_LIBRARIES["jquery"] = Library("jquery","jQuery", v, url_u, url)

v = ('1.5.2', '1.5.3',
     '1.6.0',
     '1.7.0','1.7.1', '1.7.2', '1.7.3',
     '1.8.0', '1.8.1', '1.8.2', '1.8.4', '1.8.5','1.8.6')
url_u = "https://ajax.googleapis.com/ajax/libs/jqueryui/%(version)s/jquery-ui.js"
url = "https://ajax.googleapis.com/ajax/libs/jqueryui/%(version)s/jquery-ui.min.js"
GOOGLE_LIBRARIES["jqueryui"] = Library("jqueryui","jQuery UI", v, url_u, url)

v = ('1.1.1', '1.1.2', '1.2.1', '1.2.2', '1.2.3', '1.2.4', '1.2.5','1.3.0')
url_u = "https://ajax.googleapis.com/ajax/libs/mootools/%(version)s/mootools.js"
url = "https://ajax.googleapis.com/ajax/libs/mootools/%(version)s/mootools-yui-compressed.js"
GOOGLE_LIBRARIES["mootools"] =  Library("mootools","MooTools", v, url_u, url)

v = ('1.6.0.2', '1.6.0.3', '1.6.1.0','1.7.0.0')
url_u = "https://ajax.googleapis.com/ajax/libs/prototype/%(version)s/prototype.js"
url = "https://ajax.googleapis.com/ajax/libs/prototype/%(version)s/prototype.js"
GOOGLE_LIBRARIES["prototype"] = Library("prototype","Prototype", v, url_u, url)

v = ('1.8.1', '1.8.2','1.8.3')
url_u = "https://ajax.googleapis.com/ajax/libs/scriptaculous/%(version)s/scriptaculous.js"
url = "https://ajax.googleapis.com/ajax/libs/scriptaculous/%(version)s/scriptaculous.js"
lib = Library("scriptaculous","script.aculo.us", v, url_u, url)
GOOGLE_LIBRARIES["scriptaculous"] = lib

v = ('2.1','2.2')
url_u = "https://ajax.googleapis.com/ajax/libs/swfobject/%(version)s/swfobject_src.js"
url = "https://ajax.googleapis.com/ajax/libs/swfobject/%(version)s/swfobject.js"
GOOGLE_LIBRARIES["swfobject"] = Library("swfobject","SWFObject", v, url_u, url)

v = ('2.6.0', '2.7.0', '2.8.0r4', '2.8.1','2.8.2')
url_u = "https://ajax.googleapis.com/ajax/libs/yui/%(version)s/build/yuiloader/yuiloader.js"
url = "https://ajax.googleapis.com/ajax/libs/yui/%(version)s/build/yuiloader/yuiloader-min.js"
lib = Library("yui","Yahoo! User Interface Library (YUI)", v, url_u, url)
GOOGLE_LIBRARIES["yui"] = lib


class LibraryWidget(ASCIIWidget):
    """Library widget"""

    type = 'library'

    def hasInput(self):
        return (self.name+'.id' in self.request.form and
                self.name+'.version' in self.request.form)

    def _getFormInput(self):
        url = self.request.get(self.name+'.id').strip()
        key = self.request.get(self.name+'.version').strip()
        return "%s | %s" % (url, key)

    def __call__(self):
        value = self._getFormValue()
        if type(value) == Library:
            value = str(value)
        if value is None or value == self.context.missing_value:
            value = ''
        value = value.split("|")
        if len(value) == 2:
            value = (value[0].strip(), value[1].strip())
        else:
            value = ('', '')

        name = self.name + '.id'
        id = '<select id="%s" name="%s">'%(name, name)
        for i in GOOGLE_LIBRARIES.keys():
            if value[0] == i:
                id += '<option value="%s" selected="selected" />%s'%(i, i)
            else:
                id += '<option value="%s" />%s'%(i, i)
        id += '</select>'

        version = renderElement(self.tag,
                            type=self.type,
                            name=self.name+'.version',
                            id=self.name+'.version',
                            value=value[1],
                            cssClass=self.cssClass,
                            size=8,
                            extra=self.extra)

        return "%s %s" % (id, version)



class LibraryManager(SchemaAdapterBase):
    """The library manager. manage CRUD on Library"""
    component.adapts(IPloneSiteRoot)
    interface.implements(interfaces.ILibraryManager)

    def __init__(self, context):
        self.context = context
        self.loader_mode = "scripttags"

    def get_libraries(self):
        res = []
        conf = getattr(self.properties, config.PROPERTY_LIBRARIES_FIELD, '')
        self.context.plone_log('get ' + str(conf))

        for lib in conf:
            value = lib.split('|')
            libname = value[0].strip()
            library = GOOGLE_LIBRARIES.get(libname,None)
            if library is None:
                continue
            version = value[1].strip()
            if version:
                library.version = version
            res.append(library)

        return tuple(res)

    def set_libraries(self, value):
        self.context.plone_log('set ' + str(value))
        self.properties._updateProperty(config.PROPERTY_LIBRARIES_FIELD, value)

    libraries = property(get_libraries, set_libraries)

    @property
    def properties(self):
        return getToolByName(self.context, 'portal_properties').google_properties
