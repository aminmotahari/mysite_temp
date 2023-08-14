from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .forms import NameForm, ContactForm, NewsLetterForm
from website.models import Contact
from django.shortcuts import get_object_or_404
from django.contrib import messages



def home_view(request):
    return render(request, 'website/index.html')


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form_instance = Contact()
            form_instance.name = 'unknown'
            form_instance.subject = form.cleaned_data['subject']
            form_instance.email = form.cleaned_data['email']
            form_instance.message = form.cleaned_data['message']
            form_instance.save()
            print('salam')
            #form.save()
            messages.add_message(request, messages.SUCCESS, "Submitted succesfully.")
        else:
            messages.add_message(request, messages.ERROR, "Unsucesful submission.")
    form = ContactForm()
    return render(request, 'website/contact.html')


def about_view(request):
    return render(request, 'website/about.html')

def NewsLetter_view(request):
    if request.method == "POST":
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")

def test_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("thanks")
        else:
            return HttpResponse("Not Valid")

    form = ContactForm()
    return render(request, "test.html", {"form": form})