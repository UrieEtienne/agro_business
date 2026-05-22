from django.shortcuts import render, redirect

from .models import Contact
from .forms import ContactForm


def contact(request):

    contact_info = Contact.objects.first()

    form = ContactForm()

    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('contact')

    context = {
        'contact': contact_info,
        'form': form
    }

    return render(request, 'contact/contact.html', context)