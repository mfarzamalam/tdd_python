from datetime import timedelta
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest, request

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
        request  = HttpRequest()
        response = home_page(request)
        html     = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))