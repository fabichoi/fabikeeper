from flask_restx import Namespace, fields
from fabikeeper.models.label import Label as LabelModel

ns = Namespace(
    'labels',
    description='라벨 관련 API'
)

label = ns.model('Label', {
    'id': fields.Integer(required=True, description='라벨 고유 아이디'),
    'user_id': fields.Integer(required=True, description='라벨 작성자 유저 고유 아이디'),
    'content': fields.Integer(required=True, description='라벨 내용'),
    'created_at': fields.Integer(escription='라벨 생성 일자'),
})
