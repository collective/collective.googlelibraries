from zope import interface
from collective.googlelibraries import interfaces

class Library(object):
    interface.implements(interfaces.ILibrary)
    def __init__(self, id, title, version, url_u, url):
        self.id = id
        self.title = title
        self.version = version
        self._url_u = url_u
        self._url = url
        self.mode = 'minified'

    @property
    def url(self):
        if self.mode != 'minified':
            return self._url_u
        return self._url

GOOGLE_LIBRARIES = {}

GOOGLE_LIBRARIES["chrome-frame"] = {}
for v in ('1.0.0', '1.0.1', '1.0.2'):
    url = "https://ajax.googleapis.com/ajax/libs/chrome-frame/%s/CFInstall.min.js"%v
    url_u = "https://ajax.googleapis.com/ajax/libs/chrome-frame/%s/CFInstall.js"%v
    GOOGLE_LIBRARIES["chrome-frame"][v] = Library("chrome-frame","Chrome Frame", v, url_u, url)

GOOGLE_LIBRARIES["dojo"] = {}
for v in ('1.1.1',
          '1.2.0', '1.2.3',
          '1.3.0', '1.3.1', '1.3.2',
          '1.4.0', '1.4.1', '1.4.3',
          '1.5'):
    url_u = "https://ajax.googleapis.com/ajax/libs/dojo/%s/dojo/dojo.xd.js.uncompressed.js"%v
    url = "https://ajax.googleapis.com/ajax/libs/dojo/%s/dojo/dojo.xd.js"%v
    GOOGLE_LIBRARIES["dojo"][v] = Library("dojo","Dojo", v, url_u, url)

GOOGLE_LIBRARIES["ext-core"] = {}
for v in ('3.0.0','3.1.0'):
    url_u = "https://ajax.googleapis.com/ajax/libs/ext-core/%s/ext-core-debug.js"%v
    url = "https://ajax.googleapis.com/ajax/libs/ext-core/%s/ext-core.js"%v
    GOOGLE_LIBRARIES["ext-core"][v] = Library("ext-core","Ext Core", v, url_u, url)

GOOGLE_LIBRARIES["jquery"] = {}
for v in ('1.2.3', '1.2.6',
          '1.3.0', '1.3.1', '1.3.2',
          '1.4.0', '1.4.1', '1.4.2','1.4.3','1.4.4'):
    url_u = "https://ajax.googleapis.com/ajax/libs/jquery/%s/jquery.js"%v
    url = "https://ajax.googleapis.com/ajax/libs/jquery/%s/jquery.min.js"%v
    GOOGLE_LIBRARIES["jquery"][v] = Library("jquery","jQuery", v, url_u, url)

GOOGLE_LIBRARIES["jqueryui"] = {}
for v in ('1.5.2', '1.5.3',
          '1.6.0',
          '1.7.0','1.7.1', '1.7.2', '1.7.3',
          '1.8.0', '1.8.1', '1.8.2', '1.8.4', '1.8.5','1.8.6'):
    url_u = "https://ajax.googleapis.com/ajax/libs/jqueryui/%s/jquery-ui.js"%v
    url = "https://ajax.googleapis.com/ajax/libs/jqueryui/%s/jquery-ui.min.js"%v
    GOOGLE_LIBRARIES["jqueryui"][v] = Library("jqueryui","jQuery UI", v, url_u, url)

GOOGLE_LIBRARIES["mootools"] = {}
for v in ('1.1.1', '1.1.2', '1.2.1', '1.2.2', '1.2.3', '1.2.4', '1.2.5','1.3.0'):
    url_u = "https://ajax.googleapis.com/ajax/libs/mootools/%s/mootools.js"%v
    url = "https://ajax.googleapis.com/ajax/libs/mootools/%s/mootools-yui-compressed.js"%v
    GOOGLE_LIBRARIES["mootools"][v] =  Library("mootools","MooTools", v, url_u, url)

GOOGLE_LIBRARIES["prototype"] = {}
for v in ('1.6.0.2', '1.6.0.3', '1.6.1.0','1.7.0.0'):
    url_u = "https://ajax.googleapis.com/ajax/libs/prototype/%s/prototype.js"%v
    url = "https://ajax.googleapis.com/ajax/libs/prototype/%s/prototype.js"%v
    GOOGLE_LIBRARIES["prototype"][v] = Library("prototype","Prototype", v, url_u, url)

GOOGLE_LIBRARIES["scriptaculous"] = {}
for v in ('1.8.1', '1.8.2','1.8.3'):
    url_u = "https://ajax.googleapis.com/ajax/libs/scriptaculous/%s/scriptaculous.js"%v
    url = "https://ajax.googleapis.com/ajax/libs/scriptaculous/%s/scriptaculous.js"%v
    GOOGLE_LIBRARIES["scriptaculous"][v] = Library("scriptaculous","script.aculo.us", v, url_u, url)

GOOGLE_LIBRARIES["swfobject"] = {}
for v in ('2.1','2.2'):
    url_u = "https://ajax.googleapis.com/ajax/libs/swfobject/%s/swfobject_src.js"%v
    url = "https://ajax.googleapis.com/ajax/libs/swfobject/%s/swfobject.js"%v
    GOOGLE_LIBRARIES["swfobject"][v] = Library("swfobject","SWFObject", v, url_u, url)

GOOGLE_LIBRARIES["yui"] = {}
for v in ('2.6.0', '2.7.0', '2.8.0r4', '2.8.1','2.8.2'):
    url_u = "https://ajax.googleapis.com/ajax/libs/yui/%s/build/yuiloader/yuiloader.js"%v
    url = "https://ajax.googleapis.com/ajax/libs/yui/%s/build/yuiloader/yuiloader-min.js"%v
    GOOGLE_LIBRARIES["yui"][v] = Library("yui","Yahoo! User Interface Library (YUI)", v, url_u, url)


class LibraryManager(object):
    def __init__(self, context):
        self.context = context

    def add(self, library):
        pass

    def remove(self, library):
        pass

    @property
    def libraries(self):
        return []

    @property
    def available_libraries(self):
        return GOOGLE_LIBRARIES
