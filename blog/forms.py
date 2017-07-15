from django.forms import ModelForm

from blog.models import Contact


class ContactForms(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
