from django.test import TestCase
from django.urls import reverse
from .models import Post


# Create your tests here.
class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test !")

    def test_model_data(self):
        self.assertEqual(self.post.text, "This is a test !")

    # Url exists at the correct location
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page(self):
        response = self.client.get(reverse("home"))
        self.assertAlmostEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "This is a test !")
