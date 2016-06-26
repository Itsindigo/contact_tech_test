#### Contact Form  Technical Test

 - [Deployed to Heroku](https://farm-tech-test.herokuapp.com/contact/new/)

 The objective of this test was to deliver a form that accepted enquirer information, posted to a database and returned an email confirmation. Some of the conscious design decisions I made included; opting to use a ModelForm as this allowed validations to be automatically added at the model level (Ironically the final form has no validations after I discovered the EmailField), additionally using this Django functionality will reduce the number of tests to be written later as they will be using internal mechanisms.

###### Current code bugs/implementation issues.

 - The SendGrid mail server is currently stored in settings.py rather than an environment variable, definitely needs to be fixed before adding any personal details to the account.

 - The form needs more tailored validations with regards to input length, as currently it requires only that a field not be blank, and an email be an address.

###### To run this code

   - Clone
   - $ pip install -r requirements.txt
