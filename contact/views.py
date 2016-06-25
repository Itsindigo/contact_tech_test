from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import ContactForm


def contact_new(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact information saved')
            return redirect(contact_new)
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,
    })
