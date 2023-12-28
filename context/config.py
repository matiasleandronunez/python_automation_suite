import os

class Settings(object):
    """Simple singleton class for managing and accessing settings"""
    def __init__(self):
        self.url = os.environ.get('URI')
        self.api_uri = os.environ.get('API_URI')
        self.default_browser = os.environ.get('BROWSER')

settings = Settings()