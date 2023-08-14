from django import forms
from website.models import Contact, NewsLetter
from captcha.fields import CaptchaField

class NameForm(forms.Form):
    name = forms.CharField(label="name", max_length=255)
    subject = forms.CharField(label="subject", max_length=255)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'