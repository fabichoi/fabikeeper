import os.path
import sys

sys.path.append('.')
from fabikeeper.configs import TestingConfig
from fabikeeper import create_app, db
from fabikeeper.models.user import User as UserModel
import pytest


@pytest.fixture(scope='session')
def user_data():
    yield dict(
        user_id='tester',
        user_name='tester',
        password='tester'
    )


@pytest.fixture(scope='session')
def app(user_data):
    app = create_app(TestingConfig())
    with app.app_context():
        db.drop_all()
        db.create_all()
        db.session.add(UserModel(**user_data))
        db.session.commit()
        yield app

        db.drop_all()
        db_path = app.config['SQLALCHEMY_DATABASE_URI'].replace(
            'sqlite://',
            ''
        )
        if os.path.isfile(db_path):
            os.remove(db_path)


@pytest.fixture(scope='session')
def client(app, user_data):
    with app.test_client() as client:
        # 세션 적용
        with client.session_transaction() as session:
            session['user_id'] = user_data.get('user_id')
        yield client
