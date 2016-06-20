from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm


def contact_new(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://google.com')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,
    })
