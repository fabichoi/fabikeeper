from flask_restx import Namespace, Resource, fields
from fabikeeper.models.user import User as UserModel

ns = Namespace(
    'users',
    description='유저 관련 API'
)

user = ns.model('User', {
    'id': fields.Integer(required=True, description='유저 고유 번호'),
    'user_id': fields.String(required=True, description='유저 아이디'),
    'user_name': fields.String(required=True, description='유저 이름'),
})


# /api/users
@ns.route('')
class UserList(Resource):
    @ns.marshal_list_with(user, skip_none=True)
    def get(self):
        """유저 복수 조회"""
        data = UserModel.query.all()
        return data


# /api/users/1
@ns.route('/<int:id>')
@ns.param('id', '유저 고유 번호')
class User(Resource):
    @ns.marshal_list_with(user, skip_none=True)
    def get(self, id):
        """유저 단수 조회"""
        data = UserModel.query.get_or_404(id)
        return data
