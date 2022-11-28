from flask_restx import Api
from flask import Blueprint
from .user import ns as UserNamespace

blueprint = Blueprint(
    'api',
    __name__,
    url_prefix='/api'
)

api = Api(
    blueprint,
    title='FabiKeeper API',
    version='1.0',
    doc='/docs',
    description='API Documents'
)

api.add_namespace(UserNamespace)
