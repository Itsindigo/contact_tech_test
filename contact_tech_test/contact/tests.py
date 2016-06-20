from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest

from contact.views import index

class IndexTest(TestCase):

    def test_contact_url_resolves_to_index_view(self):
        found = resolve('/contact/')
        self.assertEqual(found.func, index)

    def test_index_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)

        self.assertEqual(response.status_code, 200)

    

# Create your tests here.
