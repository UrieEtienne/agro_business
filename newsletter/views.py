from django.shortcuts import redirect
from .forms import NewsletterForm

def subscribe_newsletter(request):

    if request.method == 'POST':

        form = NewsletterForm(request.POST)

        if form.is_valid():

            form.save()

    return redirect('/')