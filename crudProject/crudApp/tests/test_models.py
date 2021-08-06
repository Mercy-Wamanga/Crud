from django.test import TestCase
from crudApp.models import Article

# Create your tests here.
class ArticleModelTest(TestCase):
    def test_get_title_name_method(self):
        """
        Method must return title name
        """
        article=Article.objects.create(title="HTML Beginners",text="Gives you the basic fundamentals for HTML beginners")
        self.assertEqual(article.get_title_name(),"HTML Beginners")