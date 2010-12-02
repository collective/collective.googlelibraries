from collective.googlelibraries import libraries

class MapsLibrary(libraries.Library):
    """Google Maps library
    http://code.google.com/apis/maps
    
    notes:
    v3 doesn't need a api key
    """
    def __init__(self, version='3'):
        super(MapsLibrary, self).__init__('maps', version=version)
        self.sensor = "false"
        self.region = ""
        self.callback = ""

    @property
    def url(self):
        return "http://maps.google.com/maps/api/js?sensor=%s"%self.sensor

    def check_id(self, id):
        pass

    @property
    def versions(self):
        return ['3']
