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
    def __init__(self, id, title, url_u, url, versions, version=''):
        self.id = id
        self.title = title
        self.versions = versions
        self.version = version
        self._url = url
        self._url_u = url_u
        self.minified = True

    @property
    def url(self):
        base = self._url
        if not self.minified:
            base = self._url_u

        version = self.version
        if not self.version:
            version = self.versions[-1]

        return base%({'version':version})

    def __str__(self):
        return '%s | %s'%(self.id, self.version)

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
url_u = "https://ajax.googleapis.com/ajax/libs/dojo/%s/dojo/dojo.xd.js.uncompressed.js"
url = "https://ajax.googleapis.com/ajax/libs/dojo/%s/dojo/dojo.xd.js"
lib = Library("dojo","Dojo", v, url_u, url)
GOOGLE_LIBRARIES["dojo"] = lib

v = ('3.0.0','3.1.0')
url_u = "https://ajax.googleapis.com/ajax/libs/ext-core/%s/ext-core-debug.js"
url = "https://ajax.googleapis.com/ajax/libs/ext-core/%s/ext-core.js"
lib = Library("ext-core","Ext Core", v, url_u, url)

GOOGLE_LIBRARIES["ext-core"] = lib

v = ('1.2.3', '1.2.6',
     '1.3.0', '1.3.1', '1.3.2',
     '1.4.0', '1.4.1', '1.4.2','1.4.3','1.4.4')
url_u = "https://ajax.googleapis.com/ajax/libs/jquery/%s/jquery.js"
url = "https://ajax.googleapis.com/ajax/libs/jquery/%s/jquery.min.js"
GOOGLE_LIBRARIES["jquery"] = Library("jquery","jQuery", v, url_u, url)

v = ('1.5.2', '1.5.3',
     '1.6.0',
     '1.7.0','1.7.1', '1.7.2', '1.7.3',
     '1.8.0', '1.8.1', '1.8.2', '1.8.4', '1.8.5','1.8.6')
url_u = "https://ajax.googleapis.com/ajax/libs/jqueryui/%s/jquery-ui.js"
url = "https://ajax.googleapis.com/ajax/libs/jqueryui/%s/jquery-ui.min.js"
GOOGLE_LIBRARIES["jqueryui"] = Library("jqueryui","jQuery UI", v, url_u, url)

v = ('1.1.1', '1.1.2', '1.2.1', '1.2.2', '1.2.3', '1.2.4', '1.2.5','1.3.0')
url_u = "https://ajax.googleapis.com/ajax/libs/mootools/%s/mootools.js"
url = "https://ajax.googleapis.com/ajax/libs/mootools/%s/mootools-yui-compressed.js"
GOOGLE_LIBRARIES["mootools"] =  Library("mootools","MooTools", v, url_u, url)

v = ('1.6.0.2', '1.6.0.3', '1.6.1.0','1.7.0.0')
url_u = "https://ajax.googleapis.com/ajax/libs/prototype/%s/prototype.js"
url = "https://ajax.googleapis.com/ajax/libs/prototype/%s/prototype.js"
GOOGLE_LIBRARIES["prototype"] = Library("prototype","Prototype", v, url_u, url)

v = ('1.8.1', '1.8.2','1.8.3')
url_u = "https://ajax.googleapis.com/ajax/libs/scriptaculous/%s/scriptaculous.js"
url = "https://ajax.googleapis.com/ajax/libs/scriptaculous/%s/scriptaculous.js"
lib = Library("scriptaculous","script.aculo.us", v, url_u, url)
GOOGLE_LIBRARIES["scriptaculous"] = lib

v = ('2.1','2.2')
url_u = "https://ajax.googleapis.com/ajax/libs/swfobject/%s/swfobject_src.js"
url = "https://ajax.googleapis.com/ajax/libs/swfobject/%s/swfobject.js"
GOOGLE_LIBRARIES["swfobject"] = Library("swfobject","SWFObject", v, url_u, url)

v = ('2.6.0', '2.7.0', '2.8.0r4', '2.8.1','2.8.2')
url_u = "https://ajax.googleapis.com/ajax/libs/yui/%s/build/yuiloader/yuiloader.js"
url = "https://ajax.googleapis.com/ajax/libs/yui/%s/build/yuiloader/yuiloader-min.js"
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

    def get_loader_mode(self):
        return getattr(self.properties, config.PROPERTY_LOADER_MODE_FIELD, '')

    def set_loader_mode(self, value):
        self.properties._updateProperty(config.PROPERTY_LOADER_MODE_FIELD, value)

    loader_mode = property(get_loader_mode, set_loader_mode)

    def get_libraries(self):
        res = []
        conf = getattr(self.properties, config.PROPERTY_LIBRARIES_FIELD, '')
        self.context.plone_log('get ' + str(conf))

        for lib in conf:
            value = lib.split('|')
            libname = value[0].strip()
            library = GOOGLE_LIBRARIES[libname]
            version = value[1].strip()
            if version:
                library.version = version
            res.append(library)
        return conf
#        return tuple(res)

    def set_libraries(self, value):
        self.context.plone_log('set ' + str(value))
        self.properties._updateProperty(config.PROPERTY_LIBRARIES_FIELD, value)

    libraries = property(get_libraries, set_libraries)

    @property
    def properties(self):
        return getToolByName(self.context, 'portal_properties').google_properties

    @property
    def libraries_dict(self):
        res = {}

        for lib in self.libraries:
            value = lib.split('|')
            libname = value[0].strip()
            library = GOOGLE_LIBRARIES[libname]
            version = value[1].strip()
            if version:
                library.version = version
            res[libname] = library

        return res
