import unittest
from .base import BaseTestCase
from mygamesite.routes import Post

class PostTests(BaseTestCase):

    # Ensure a logged in user can add a new post
    def test_user_can_post(self):
        with self.client:
            self.client.post(
                '/login',
                data=dict(username="Shashh", password="testing"),
                follow_redirects=True
            )
            response = self.client.post(
                '/post',
                data=dict(title="My First Update Post", description="test"),
                follow_redirects=True
            )
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'You post has been created',
                          response.data)


 # Ensure a logged in user can update  a new post
    def test_user_can_post(self):
        with self.client:
            self.client.post(
                '/login',
                data=dict(username="Shashh", password="testing"),
                follow_redirects=True
            )
            response = self.client.post(
                '/post',
                data=dict(title="My First Update Post", description="update "),
                follow_redirects=True
            )
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Your post has been updated',
                          response.data)

    # Ensure a logged in user can delete a new post
    def test_user_can_post(self):
        with self.client:
            self.client.post(
                '/login',
                data=dict(username="Shashh", password="testing"),
                follow_redirects=True
            )
            response = self.client.post(
                '/post',
                data=dict(title="My First Update Post", description="delete"),
                follow_redirects=True
            )
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'You post has been deleted',
                          response.data)



if __name__ == '__main__':
    unittest.main()