import json

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
    def __init__(self, id, version=''):
        self.check_id(id)
        self.id = id
        self._version = version
        self._optionalSettings = {}
        self.minified = True

    def check_id(self, id):
        if id not in GOOGLE_LIBRARIES_KEYS:
            raise KeyError

    @property
    def url(self):
        base = GOOGLE_LIBRARIES[self.id]['url']
        if not self.minified:
            base = GOOGLE_LIBRARIES[self.id]['url_u']

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
        base = '%s | %s | '%(self.id, self.version)
        if self.minified:
            return base + 'minified'
        else:
            return base

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

    @property
    def versions(self):
        return GOOGLE_LIBRARIES[self.id]['versions']

    def settings_schema(self):
        return GoogleLibrarySettingsSchema

class GoogleLibrarySettingsSchema(interface.Interface):
    """The only option available on all libraries is the minified
    option
    """

    minified = schema.Bool(title=_("label_minified", default="Minified"))

#Now lets define all available libraries
GOOGLE_LIBRARIES = {}
GOOGLE_LIBRARIES['chrome-frame'] = {}
GOOGLE_LIBRARIES['chrome-frame']['versions'] = ('1.0.0', '1.0.1', '1.0.2')
GOOGLE_LIBRARIES['chrome-frame']['url'] = "https://ajax.googleapis.com/ajax/libs/chrome-frame/%(version)s/CFInstall.min.js"
GOOGLE_LIBRARIES['chrome-frame']['url_u'] = "https://ajax.googleapis.com/ajax/libs/chrome-frame/%(version)s/CFInstall.js"

GOOGLE_LIBRARIES["dojo"] = {}
GOOGLE_LIBRARIES["dojo"]['versions'] = ('1.1.1',
      '1.2.0', '1.2.3',
      '1.3.0', '1.3.1', '1.3.2',
      '1.4.0', '1.4.1', '1.4.3',
      '1.5')
GOOGLE_LIBRARIES["dojo"]['url_u'] = "https://ajax.googleapis.com/ajax/libs/dojo/%(version)s/dojo/dojo.xd.js.uncompressed.js"
GOOGLE_LIBRARIES["dojo"]['url'] = "https://ajax.googleapis.com/ajax/libs/dojo/%(version)s/dojo/dojo.xd.js"

GOOGLE_LIBRARIES["ext-core"] = {}
GOOGLE_LIBRARIES["ext-core"]['versions'] = ('3.0.0','3.1.0')
GOOGLE_LIBRARIES["ext-core"]['url_u'] = "https://ajax.googleapis.com/ajax/libs/ext-core/%(version)s/ext-core-debug.js"
GOOGLE_LIBRARIES["ext-core"]['url'] = "https://ajax.googleapis.com/ajax/libs/ext-core/%(version)s/ext-core.js"

GOOGLE_LIBRARIES["jquery"] = {}
GOOGLE_LIBRARIES["jquery"]['versions'] = ('1.2.3', '1.2.6',
     '1.3.0', '1.3.1', '1.3.2',
     '1.4.0', '1.4.1', '1.4.2','1.4.3','1.4.4')
GOOGLE_LIBRARIES["jquery"]['url_u'] = "https://ajax.googleapis.com/ajax/libs/jquery/%(version)s/jquery.js"
GOOGLE_LIBRARIES["jquery"]['url'] = "https://ajax.googleapis.com/ajax/libs/jquery/%(version)s/jquery.min.js"

GOOGLE_LIBRARIES["jqueryui"] = {}
GOOGLE_LIBRARIES["jqueryui"]['versions'] = ('1.5.2', '1.5.3',
     '1.6.0',
     '1.7.0','1.7.1', '1.7.2', '1.7.3',
     '1.8.0', '1.8.1', '1.8.2', '1.8.4', '1.8.5','1.8.6')
GOOGLE_LIBRARIES["jqueryui"]['url_u'] = "https://ajax.googleapis.com/ajax/libs/jqueryui/%(version)s/jquery-ui.js"
GOOGLE_LIBRARIES["jqueryui"]['url'] = "https://ajax.googleapis.com/ajax/libs/jqueryui/%(version)s/jquery-ui.min.js"

GOOGLE_LIBRARIES["mootools"] = {}
GOOGLE_LIBRARIES["mootools"]['versions'] = ('1.1.1', '1.1.2', '1.2.1', '1.2.2', '1.2.3', '1.2.4', '1.2.5','1.3.0')
GOOGLE_LIBRARIES["mootools"]['url_u'] = "https://ajax.googleapis.com/ajax/libs/mootools/%(version)s/mootools.js"
GOOGLE_LIBRARIES["mootools"]['url'] = "https://ajax.googleapis.com/ajax/libs/mootools/%(version)s/mootools-yui-compressed.js"

GOOGLE_LIBRARIES["prototype"] = {}
GOOGLE_LIBRARIES["prototype"]['versions'] = ('1.6.0.2', '1.6.0.3', '1.6.1.0','1.7.0.0')
GOOGLE_LIBRARIES["prototype"]['url_u'] = "https://ajax.googleapis.com/ajax/libs/prototype/%(version)s/prototype.js"
GOOGLE_LIBRARIES["prototype"]['url'] = "https://ajax.googleapis.com/ajax/libs/prototype/%(version)s/prototype.js"

GOOGLE_LIBRARIES["scriptaculous"] = {}
GOOGLE_LIBRARIES["scriptaculous"]['versions'] = ('1.8.1', '1.8.2','1.8.3')
GOOGLE_LIBRARIES["scriptaculous"]['url_u'] = "https://ajax.googleapis.com/ajax/libs/scriptaculous/%(version)s/scriptaculous.js"
GOOGLE_LIBRARIES["scriptaculous"]['url'] = "https://ajax.googleapis.com/ajax/libs/scriptaculous/%(version)s/scriptaculous.js"

GOOGLE_LIBRARIES["swfobject"] = {}
GOOGLE_LIBRARIES["swfobject"]['versions'] = ('2.1','2.2')
GOOGLE_LIBRARIES["swfobject"]['url_u'] = "https://ajax.googleapis.com/ajax/libs/swfobject/%(version)s/swfobject_src.js"
GOOGLE_LIBRARIES["swfobject"]['url'] = "https://ajax.googleapis.com/ajax/libs/swfobject/%(version)s/swfobject.js"

GOOGLE_LIBRARIES["yui"] = {}
GOOGLE_LIBRARIES["yui"]['versions'] = ('2.6.0', '2.7.0', '2.8.0r4', '2.8.1','2.8.2')
GOOGLE_LIBRARIES["yui"]['url_u'] = "https://ajax.googleapis.com/ajax/libs/yui/%(version)s/build/yuiloader/yuiloader.js"
GOOGLE_LIBRARIES["yui"]['url'] = "https://ajax.googleapis.com/ajax/libs/yui/%(version)s/build/yuiloader/yuiloader-min.js"

GOOGLE_LIBRARIES_KEYS = GOOGLE_LIBRARIES.keys()


class LibraryWidget(ASCIIWidget):
    """Library widget"""

    type = 'library'

    def hasInput(self):
        return (self.name+'.id' in self.request.form and
                self.name+'.version' in self.request.form and
                self.name+'.settings')

    def _getFormInput(self):
        url = self.request.get(self.name+'.id').strip()
        key = self.request.get(self.name+'.version').strip()
        settings = self.request.get(self.name+'.settings', 'uncompressed')
        return "%s | %s | %s" % (url, key, settings)

    def __call__(self):
        #build value for input in widget
        value = self._getFormValue()
        if type(value) == Library:
            value = str(value)
        elif value is None or value == self.context.missing_value:
            value = ''

        value = value.split("|")
        if len(value) == 3:
            value = (value[0].strip(), value[1].strip(), value[2].strip())
        else:
            value = ('', '', '')

        #render
        lib = self.render_libchoice(name, value[0])
        version = self.render_version(value[1])
        settings = self.render_settings(value[2])

        return "%s %s %s" % (lib, version, settings)

    def render_libchoice(self, value=''):
        name = self.tag + '.id'
        rendered = '<select id="%s" name="%s">'%(name, name)
        for i in GOOGLE_LIBRARIES_KEYS:
            if i == value:
                rendered += '<option value="%s" selected="selected" />%s'%(i, i)
            else:
                rendered += '<option value="%s" />%s'%(i, i)
        rendered += '</select>'

        return rendered

    def render_version(self, value=''):
        return renderElement(self.tag,
                            type='text',
                            name=self.name+'.version',
                            id=self.name+'.version',
                            value=value,
                            cssClass=self.cssClass,
                            size=8,
                            extra=self.extra)

    def render_settings(self, value=''):
        name = self.name + '.settings'
        settings = '<input type="checkbox" id="%s" name="%s" value="minified" %s /> minified'

        if not value or value == 'minified':
            minified = 'checked="checked"'
        elif value and value != 'minified':
            minified = ''
        return settings%(name, name, minified)

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

        for lib in conf:
            value = lib.split('|')
            libname = value[0].strip()
            if libname not in GOOGLE_LIBRARIES_KEYS:
                continue
            library = Library(libname)
            version = value[1].strip()
            if version:
                library.version = version
            settings = value[2].strip()
            if settings and settings != 'minified':
                library.minified = False

            res.append(library)

        return tuple(res)

    def set_libraries(self, value):
        res = []

        if type(value) not in (tuple, list):
            return

        for lib_version in value:
            stripped = [a.strip() for a in lib_version.split('|')]
            lib = version = settings = ''
            if len(stripped) == 1:
                lib, = stripped
            elif len(stripped) == 2:
                lib, version = stripped
            elif len(stripped) == 3:
                lib, version, settings = stripped
            else:
                contine
            if lib not in GOOGLE_LIBRARIES_KEYS:
                continue
            elif not version:
                version = GOOGLE_LIBRARIES[lib]['versions'][-1]
            elif version not in GOOGLE_LIBRARIES[lib]['versions']:
                continue
            if settings != 'minified':
                settings = 'uncompressed'
            res.append('%s | %s | %s'%(lib, version, settings))

        value = tuple(res)
        self.properties._updateProperty(config.PROPERTY_LIBRARIES_FIELD, value)

    libraries = property(get_libraries, set_libraries)

    @property
    def properties(self):
        return getToolByName(self.context, 'portal_properties').google_properties
