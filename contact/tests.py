from django.test import TestCase, Client
from django.core import mail
from django.core.urlresolvers import resolve, reverse
from django.http import HttpRequest

from contact.models import ContactType
from contact.forms import ContactForm
from contact.views import contact_new
from .models import Contact

class ContactFormTest(TestCase):

    def setUp(self):
        self.client = Client()
        type1 = ContactType(_type="Enquiry Type 1")
        type1.save()

        type2 = ContactType(_type="Enquiry Type 2")
        type2.save()


    def test_contact_url_resolves_to_contact_view(self):
        found = resolve('/contact/new/')
        self.assertEqual(found.func, contact_new)

    def test_contact_returns_correct_html(self):
        request = HttpRequest()
        response = contact_new(request)
        self.assertEqual(response.status_code, 200)

    def test_valid_form_POST_returns_200_and_saved_to_db(self):
        response = self.client.post(reverse('contact_new'), {
                     'contact_name': 'something',
                     'contact_email': 'test@test.com',
                     'contact_content': 'anything',
                     'enquiry_type': '1'},
                     follow=True,)
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(response.status_code, 200)

    def test_invalid_params_does_not_create_object(self):
        response = self.client.post(reverse('contact_new'), {
                     'contact_name': 'something',
                     'contact_email': 'not-an-email'},
                     follow=True,)
        self.assertEqual(Contact.objects.count(), 0)

class ContactModelTest(TestCase):

    def test_contact_model_is_saved(self):
        contact_1 = Contact.objects.create(contact_name="Matt")
        contact_2 = Contact.objects.create(contact_name="Matthew")
        collection = Contact.objects.all()

        self.assertEqual(collection[0].contact_name, 'Matt')
        self.assertEqual(collection[1].contact_name, 'Matthew')

# class EmailSendingTest(TestCase):

    # def test_an_email_is_sent(self):
    #     user_input = {'contact_name': 'Matthew',
    #              'contact_email': 'matt@test.com',
    #              'contact_content': 'Some text',
    #              'enquiry_type': 'General Enquiry'}
    #
    #     self.response = self.client.post(
    #             reverse('contact_new'),
    #             data=user_input,
    #             )
    #
    #     self.assertEqual(len(mail.outbox), 1)
    #     self.assertEqual(mail.outbox[0].subject, 'You received a contact form submission.')
