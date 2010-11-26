from zope import interface
from collective.googlelibraries import interfaces

class Library(object):
    interface.implements(interfaces.ILibrary)
    def __init__(self, id, title, version, url, url_min):
        self.id = id
        self.title = title
        self.version = version
        self.url = url
        self.url_min = url_min

GOOGLE_LIBRARIES = []

for v in ('1.0.0', '1.0.1', '1.0.2'):
    url_min = "https://ajax.googleapis.com/ajax/libs/chrome-frame/%s/CFInstall.min.js"%v
    url = "https://ajax.googleapis.com/ajax/libs/chrome-frame/%s/CFInstall.js"%v
    GOOGLE_LIBRARIES.append(Library("chrome-frame","Chrome Frame", v, url, url_min))

for v in ('1.1.1',
          '1.2.0', '1.2.3',
          '1.3.0', '1.3.1', '1.3.2',
          '1.4.0', '1.4.1', '1.4.3',
          '1.5'):
    url = "https://ajax.googleapis.com/ajax/libs/dojo/%s/dojo/dojo.xd.js.uncompressed.js"%v
    url_min = "https://ajax.googleapis.com/ajax/libs/dojo/%s/dojo/dojo.xd.js"%v
    GOOGLE_LIBRARIES.append(Library("dojo","Dojo", v, url, url_min))

for v in ('3.0.0','3.1.0'):
    url = "https://ajax.googleapis.com/ajax/libs/ext-core/%s/ext-core-debug.js"%v
    url_min = "https://ajax.googleapis.com/ajax/libs/ext-core/%s/ext-core.js"%v
    GOOGLE_LIBRARIES.append(Library("ext-core","Ext Core", v, url, url_min))

for v in ('1.2.3', '1.2.6',
          '1.3.0', '1.3.1', '1.3.2',
          '1.4.0', '1.4.1', '1.4.2','1.4.3','1.4.4'):
    url = "https://ajax.googleapis.com/ajax/libs/jquery/%s/jquery.js"%v
    url_min = "https://ajax.googleapis.com/ajax/libs/jquery/%s/jquery.min.js"%v
    GOOGLE_LIBRARIES.append(Library("jquery","jQuery", v, url, url_min))
for v in ('1.5.2', '1.5.3',
          '1.6.0',
          '1.7.0','1.7.1', '1.7.2', '1.7.3',
          '1.8.0', '1.8.1', '1.8.2', '1.8.4', '1.8.5','1.8.6'):
    url = "https://ajax.googleapis.com/ajax/libs/jqueryui/%s/jquery-ui.js"%v
    url_min = "https://ajax.googleapis.com/ajax/libs/jqueryui/%s/jquery-ui.min.js"%v
    GOOGLE_LIBRARIES.append(Library("jqueryui","jQuery UI", v, url, url_min))

for v in ('1.1.1', '1.1.2', '1.2.1', '1.2.2', '1.2.3', '1.2.4', '1.2.5','1.3.0'):
    url = "https://ajax.googleapis.com/ajax/libs/mootools/%s/mootools.js"%v
    url_min = "https://ajax.googleapis.com/ajax/libs/mootools/%s/mootools-yui-compressed.js"%v
    GOOGLE_LIBRARIES.append(Library("mootools","MooTools", v, url, url_min))

for v in ('1.6.0.2', '1.6.0.3', '1.6.1.0','1.7.0.0'):
    url = "https://ajax.googleapis.com/ajax/libs/prototype/%s/prototype.js"%v
    url_min = "https://ajax.googleapis.com/ajax/libs/prototype/%s/prototype.js"%v
    GOOGLE_LIBRARIES.append(Library("prototype","Prototype", v, url, url_min))

for v in ('1.8.1', '1.8.2','1.8.3'):
    url = "https://ajax.googleapis.com/ajax/libs/scriptaculous/%s/scriptaculous.js"%v
    url_min = "https://ajax.googleapis.com/ajax/libs/scriptaculous/%s/scriptaculous.js"%v
    GOOGLE_LIBRARIES.append(Library("scriptaculous","script.aculo.us", v, url, url_min))

for v in ('2.1','2.2'):
    url = "https://ajax.googleapis.com/ajax/libs/swfobject/%s/swfobject_src.js"%v
    url_min = "https://ajax.googleapis.com/ajax/libs/swfobject/%s/swfobject.js"%v
    GOOGLE_LIBRARIES.append(Library("swfobject","SWFObject", v, url, url_min))

for v in ('2.6.0', '2.7.0', '2.8.0r4', '2.8.1','2.8.2'):
    url = "https://ajax.googleapis.com/ajax/libs/yui/%s/build/yuiloader/yuiloader.js"%v
    url_min = "https://ajax.googleapis.com/ajax/libs/yui/%s/build/yuiloader/yuiloader-min.js"%v
    GOOGLE_LIBRARIES.append(Library("yui","Yahoo! User Interface Library (YUI)", v, url, url_min))



class LibraryManager(object):
    def __init__(self, context):
        self.context = context

    def add(self, library):
        pass

    def remove(self, library):
        pass

    def libraries(self):
        return []

    def available_libraries(self):
        return GOOGLE_LIBRARIES
