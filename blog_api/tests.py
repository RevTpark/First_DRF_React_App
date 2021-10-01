from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Category, Post
from django.contrib.auth.models import User
from rest_framework.test import APIClient

# Create your tests here.
class PostTests(APITestCase):

    def test_view_posts(self):
        url = reverse("blog_api:list_create")
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def create_post(self):
        self.test_category = Category.objects.create(name="django")
        self.testuser1 = User.objects.create_superuser(username="test_user1", password="12345")
        self.client.login(username="test_user1", password="12345")
        data = {"title": "new", "author": 1, "excerpt": "new", "content": "new"}
        url = reverse("blog_api:list_create")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_update(self):
        client = APIClient()
        self.test_category = Category.objects.create(name="django")
        self.testuser1 = User.objects.create_user(username="test_user1", password="12345")
        self.testuser2 = User.objects.create_superuser(username="test_user2", password="12345")
        client.login(username=self.testuser1.username, password="12345")
        test_post = Post.objects.create(category_id=1, title="Post Title", excerpt="Post Excerpt",
                                        content="Post Content", slug="post-title", author_id=1, status="published")
        url = reverse("blog_api:detail_create", kwargs={"pk": 1})
        response = client.put(
            url, {
                "id": 1,
                "title": "New",
                "author": 1,
                "excerpt": "New",
                "content": "New",
                "status": "published"
            }, format="json"
        )
        #print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
