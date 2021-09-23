from datetime import timedelta
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest, request, response

from lists.views import home_page

# Create your tests here.
# class SmokeTest(TestCase):

#     def test_wrong_math(self):
#         self.assertEqual(1+1, 4)


class HomePageTest(TestCase):

    def test_root_url_show_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    def test_home_page_return_correct_html(self):
        response = self.client.get('/')

        html     = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))

        self.assertTemplateUsed(response, 'lists/home.html')


    def test_uses_home_page(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')