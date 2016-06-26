from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm


def contact_new(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            contact_name = cleaned.get('contact_name')
            contact_email = cleaned.get('contact_email')
            contact_content = cleaned.get('contact_content')
            contact_type = cleaned['enquiry_type']._type
            messages.success(request, 'Your message has been saved, a member of our team will be in contact soon.')

            message = "Name: %s,\n Email: %s,\n Content: %s,\n Type: %s" % (contact_name, contact_email, contact_content, contact_type)
            send_mail(
                'You received a contact form submission.',
                message,
                'autoresponse@farm.com',
                ['mattbridgesbusiness@gmail.com'],
                fail_silently=False)

            form.save()
            return redirect(contact_new)
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,
    })
