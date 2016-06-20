from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('/usr/local/bin/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_retrieve_contact_form(self):
        self.browser.get('http://localhost:8000/contact/new/')
        self.assertEqual(self.browser.title, 'Contact form')

        # self.fail('Finish the test!')
