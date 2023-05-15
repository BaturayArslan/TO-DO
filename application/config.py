from datetime import timedelta

class BaseConfig:
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=1)
    JWT_TOKEN_LOCATION = ['headers']

class TestConfig(BaseConfig):
    TESTING = True
    JWT_SECRET_KEY = 'itach1'
    
class DevConfig(BaseConfig):
    DEBUG = True