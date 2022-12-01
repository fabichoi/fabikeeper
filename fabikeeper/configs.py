class Config:
    """Flask Config"""
    SECRET_KEY = 'my_secret_key'
    SESSION_COOKIE_NAME = 'fabikeeper'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/fabikeeper?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER_UI_DOC_EXPANSION = 'list'


class DevelopmentConfig(Config):
    """Flask Config for Dev"""
    DEBUG = True
    SEND_FILE_MAX_AGE_DEFAULT = 1
    WTF_CSRF_ENABLED = False


class ProductionConfig(DevelopmentConfig):
    DEBUG = False
