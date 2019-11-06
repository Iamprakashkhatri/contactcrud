# from django.core.validators import validate_slug,validate_email
from django import forms
from . models import Contact
from . validations import validate_domainonly_email,validate_blacklisted

class ContactForm(forms.Form):
    name=forms.CharField(validators=[validate_blacklisted])
    email=forms.EmailField(validators=[validate_domainonly_email])
    address=forms.CharField()
    phone=forms.CharField()

    # def clean_name(self):
    #     name=self.cleaned_data.get('name')
    #     if name.lower()=='hari':
    #         raise forms.ValidationError("This is not a valid name")
    #     return name


    # def clean_email(self):
    #     '''
    #     Field level validation--field error
    #     '''
    #     email_passed=self.cleaned_data.get("email")
    #     email_req="hari@gmail.com"
    #     if not email_req in email_passed:
    #         raise forms.ValidationError("Not a valid email, please")
    #     return email_passed
    # def clean(self):
    #     '''
    #     Form level validation--form error
    #     '''
    #     cleaned_data=super(ContactForm,self).clean()
    #     email_passed = cleaned_data.get("email")
    #     email_req = "hari@gmail.com"
    #     if not email_req in email_passed:
    #         raise forms.ValidationError("Not a valid email, please")
    #     return email_passed
