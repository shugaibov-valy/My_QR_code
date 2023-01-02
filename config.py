import os


class DevConfig:
    DEBUG = os.environ.get('DEBUG', True)
    PORT = os.environ.get('PORT', 3052)
    HOST = os.environ.get('HOST', '0.0.0.0')
    VERSION = '0.0.1'