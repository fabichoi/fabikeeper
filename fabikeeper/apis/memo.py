from flask import g

from fabikeeper.models.user import User as UserModel
from fabikeeper.models.memo import Memo as MemoModel
from flask_restx import Namespace, fields, Resource

ns = Namespace(
    'memos',
    description='메모 관련 API'
)

memo = ns.model('Memo', {
    'id': fields.Integer(required=True, description='메모 고유 아이디'),
    'user_id': fields.Integer(required=True, description='유저 고유 아이디'),
    'title': fields.String(required=True, description='메모 제목'),
    'content': fields.String(required=True, description='메모 내용'),
    'created_at': fields.DateTime(description='메모 작성일'),
    'updated_at': fields.DateTime(description='메모 변경일'),
})


@ns.route('')
class MemoList(Resource):

    @ns.marshal_list_with(memo, skip_none=True)
    def get(self):
        '''메모 복수 조회'''
        data = MemoModel.query.join(
            UserModel,
            UserModel.id == MemoModel.user_id
        ).filter(
            UserModel.id == g.user.id
        ).order_by(
            MemoModel.created_at.desc()
        ).limit(10).all()

        return data


@ns.param('id', '메모 고유 아이디')
@ns.route('/<int:id>')
class Memo(Resource):

    @ns.marshal_list_with(memo, skip_none=True)
    def get(self, id):
        '''메모 1개 조회'''
        memo = MemoModel.query.get_or_404(id)
        if g.user.id != memo.user_id:
            ns.abort(403)
        return memo
