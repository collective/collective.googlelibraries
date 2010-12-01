from collective.googlelibraries import libraries

class GoogleAPI(libraries.Library):
    def __init__(self, name, version):
        super(GoogleAPI, self).__init__(name, name, [version], version=version,
                                        '', '')
