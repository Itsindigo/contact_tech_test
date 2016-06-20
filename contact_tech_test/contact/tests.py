from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest

from contact.forms import ContactForm
from .models import Contact

from contact.views import contact_new

class ContactTest(TestCase):

    def test_contact_url_resolves_to_contact_view(self):
        found = resolve('/contact/new/')
        self.assertEqual(found.func, contact_new)

    def test_contact_returns_correct_html(self):
        request = HttpRequest()
        response = contact_new(request)
        self.assertEqual(response.status_code, 200)

    def test_form_accepts_valid_email_and_name(self):
        form_data = {'contact_name': 'something',
                     'contact_email': 'test@test.com'}
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_raises_error_with_invalid_email(self):
        form_data = {'contact_name': 'something',
                     'contact_email': 'not-an-email'}
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
