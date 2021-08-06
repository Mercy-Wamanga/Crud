from django.conf.urls import url
from django.http import response
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
# from django.contrib.auth.models import Article

class UserRegisterTests(TestCase):
    
    def test_register_page_is_rendered(self):
        """
        Register page is rendered on a get request
        """
        url="/register/"
        response=self.client.get('/register/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"crud/register.html")

    def test_user_registration(self):
        """
        User is registered and redirected to login page
        """
        url=reverse("register")
        response=self.client.post(url, {"username":"mercy", "email":"mercy@gmail.com", "password":"123456"})
        self.assertEqual(response.status_code,302)
        self.assertRedirects(response,reverse("login_user"), 302)


class LoginTests(TestCase):
    def test_access_login_page(self):

       """
       Access to the login page
       """
       url="/login/"
       response=self.client.get('/login/')
       self.assertEqual(response.status_code,200)
       self.assertTemplateUsed(response,"crud/login.html")
    
    def login_success(self):
       user=self.object.create_user(username="mercy", email="mercy@gmail.com", password="123456")
       response=self.client.login(username="mercy",password="123456")
       self.assertEqual(response.status_code,302)
       self.assertRedirects(response,reverse("show"), 302)

    def login_fail(self):
       user=self.object.create_user(username="mercyl", email="mercy@gmail.com", password="1234567")
       response=self.client.login(username="mercy",password="123456")
       self.assertEqual(response.status_code,401)
       self.assertTemplateUsed(response,"crud/login.html")

    def login_user_without_username(self):
       user=self.object.create_user(username="mercyl", email="mercy@gmail.com", password="1234567")
       response=self.client.login(username=" ",password="123456")
       self.assertEqual(response.status_code,200)
       self.assertTemplateUsed(response,"crud/login.html")

    

        