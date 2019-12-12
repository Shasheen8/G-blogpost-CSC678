import unittest
from flask_testing import TestCase
from mygamesite import app,db
from mygamesite.models import User,Post

class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config['TESTING']= True
        return app

    def setUp(self):
        db.create_all()
        user = User(username="Alien", email="Alien@gmail.com",password= "demo")
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
        post = Post(title="yo", content="This is a test. Only a test.", user_id= user.id)
        db.session.add(post)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()