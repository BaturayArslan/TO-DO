

class BaseConfig:
    pass

class TestConfig(BaseConfig):
    TESTING = True
    
class DevConfig(BaseConfig):
    DEBUG = True