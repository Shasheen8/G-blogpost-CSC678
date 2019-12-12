import unittest
from flask_testing import TestCase
from .base import BaseTestCase 

from mygamesite import app, db
from mygamesite.models import User,Post


class FlaskTestCase(BaseTestCase):
    # Ensure that Flask was set up correctly
    def test_index(self):
        response = self.client.get('/home', content_type='home.html')
        self.assertEqual(response.status_code, 200)
    

    # Ensure that posts show up on the main page
    def test_posts_show_up_on_main_page(self):
        response = self.client.post(
            '/login',
            data=dict(username="Shashhh", password="testing"),
            follow_redirects=True
        )
        self.assertIn(b'Login Successful.', response.data)





#test cases 

if __name__=='__main__':
    unittest.main()