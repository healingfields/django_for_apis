from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.
class BlogTest(TestCase):


    @classmethod
    def setUpTestData(cls) :
        user1 = User.objects.create_user(
            username="user1",password="abc123"
        )
        user1.save()

        post1 = Post.objects.create(
            author=user1,title="title1",body="body1"
        )
        post1.save()

    

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        title = f'{post.title}'
        body = f'{post.body}'
        author = f'{post.author}'
        self.assertEqual(author,'user1')
        self.assertEqual(body,'body1')
        self.assertEqual(title,'title1')