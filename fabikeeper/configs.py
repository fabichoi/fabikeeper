import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))


class Config:
    """Flask Config"""
    SECRET_KEY = 'my_secret_key'
    SESSION_COOKIE_NAME = 'fabikeeper'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/fabikeeper?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER_UI_DOC_EXPANSION = 'list'
    USER_STATIC_BASE_DIR = 'user_images'


class TestingConfig(Config):
    __test__ = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_PATH, "sqlite_test.db")}'
    WTF_CSRF_ENABLED = False


class DevelopmentConfig(Config):
    """Flask Config for Dev"""
    DEBUG = True
    SEND_FILE_MAX_AGE_DEFAULT = 1
    WTF_CSRF_ENABLED = False


class ProductionConfig(DevelopmentConfig):
    DEBUG = False
